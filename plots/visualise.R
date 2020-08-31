#  Load some libraries and ancillary bits
library(tidyverse)
library(showtext)
library(scales)
font_add(family = "Source Sans Pro", regular = "~/CloudStation/home/docs/fonts/Adobe CC/Source Sans Pro Regular.otf")

showtext_auto()

# Set up look and feel of ggplots
theme_update(
  text              = element_text(family = "Source Sans Pro"),
  plot.title        = element_text(size = 18),
  plot.subtitle     = element_text(size = 14),
  plot.margin       = margin(5, 10, 5, 35),
  axis.text         = element_text(size = 14),
  axis.title.x      = element_text(margin = margin(10, 0, 0, 0)),
  axis.title.y      = element_text(margin = margin(0, 10, 0, 0)),
  axis.text.y       = element_text(margin = margin(5, 5, 5, 5)),
  axis.text.x       = element_text(margin = margin(5, 5, 5, 5)),
  axis.title        = element_text(size = 14),
  strip.text        = element_text(size = 12),
  legend.text       = element_text(size = 14),
  legend.title      = element_text(size = 14),
  legend.background = element_rect(colour = "darkgrey", fill = "white"),
  legend.key        = element_rect(
                        colour = "transparent",
                        fill   = "transparent"
                      ),
)

# Read in data
elect <- read_csv("../redist/elections/4mil-const-pt0025-ban-ncontig-variance-fixed-distr1.csv",
            col_names = c(
                "index", 
                "plan_id", 
                "plan_label", 
                "distr", 
                "vote_circ", 
                "vote_sqre", 
                "total"
            ),
            col_types = "idifiii",
            skip = 1
)

# Compute vote shares and margins of vote shares
poss_winn = c("circle", "square")

# Function to compute winner; randomly pick a winner if the vote share is 
# tied. This function is specifically tailored to accepted the CIRCLE 
# vote margin only
win <- function(margin) {
  if(margin > 0) {'circle'}
  else if(margin < 0) {'square'}
  else(sample(poss_winn, 1, replace=TRUE))
}

# Tabulate some important new columns
elect <- mutate(
            elect, 
            circ_share = signif(vote_circ / total, 3), 
            sqre_share = signif(vote_sqre / total, 3)
         ) %>% mutate(
                  circ_marg = circ_share - sqre_share,
                  sqre_marg = sqre_share - circ_share
         ) %>% mutate(
                  distr_winner = as.factor(map_chr(.$circ_marg, win)
                              )
               ) %>% mutate(type = "simulated")

# Compute district winners and flag sampled plans as simulations (in contrast
# to custom-made gerrymander)
#ties <- filter(elect, circ_marg == sqre_marg)

gerry <- read_csv("../redist/elections/gerrymandered-plan.csv",
  col_names = c(
                "index", 
                "plan_id", 
                "plan_label", 
                "distr", 
                "vote_circ", 
                "vote_sqre", 
                "total"
              ),
              col_types = "idifiii",
              skip = 1
)

gerry <- mutate(
           gerry, 
           circ_share = signif(vote_circ / total, 3),
           sqre_share = signif(vote_sqre / total, 3)
         ) %>% mutate(
                  circ_marg = circ_share - sqre_share,
                  sqre_marg = sqre_share - circ_share
               ) %>% mutate(
                 distr_winner = as.factor(map_chr(.$circ_marg, win)
                           )
                     ) %>% mutate(
                             type = "gerry",
                             plan_label = 9999
                           )

# Compute relative efficiency gap for each plan
master <- bind_rows(elect, gerry)
master <- mutate(
            master,
            waste_sqre = ifelse(
                            distr_winner == "square",
                            2 * (vote_sqre - (total / 2)),
                            vote_sqre
                         ),
            waste_circ = ifelse(
                            distr_winner == "circle",
                            2 * (vote_circ - (total / 2)),
                            vote_circ
                         )
          ) %>% group_by(
                  plan_label
                ) %>% mutate(
                  reg2 = signif((sum(waste_sqre) / sum(vote_sqre)) - 
                    (sum(waste_circ) / sum(vote_circ)), 4)
                  )

master <- ungroup(master)


# Compute number of districts won by each party per plan
#by_plan <-  
#group_by(master, plan_label) %>% add_count(winner) %>% rename(win_count=n)
by_plan <- group_by(master, plan_label) %>% count(distr_winner) %>% rename(win_count=n)

# Label vector
parties <- c(circle = "Circle Party", square = "Square Party")

# Exponential function for demostration
expon <- function(x) {
  exp(-x)
}

ggplot(data.frame(x = c(0, 6)), aes(x = x)) +
  stat_function(fun = expon, colour = "#4C67A5", size = 1) +
  labs(y = "g(x)") +
  theme(
    plot.margin = margin(5, 50, 5, 5)
  )
#ggsave("../../diss/classicthesis/gfx/exp-graph.pdf", width = 6, height = 4) 



# District total populations
ggplot(master, aes(distr, total, group = distr, fill = distr, shape = type)) +
  geom_boxplot(show.legend = FALSE) +
  geom_point(data = gerry, size = 6, colour = "grey30") +
  geom_point(data = gerry, size = 3, colour = "white") +
  scale_shape_manual(values = c(16)) +
  scale_fill_manual(name = "District", values = c(
    "#63C2A9",
    "#FD8C62",
    "#8E9FCC",
    "#E889C3",
    "#A7D855",
    "#FFD930"
  )) +
  guides(
    fill = guide_legend(
      override.aes = list(
        size = 6,
        colour = c(
          "#63C2A9",
          "#FD8C62",
          "#8E9FCC",
          "#E889C3",
          "#A7D855",
          "#FFD930"
        ),
        shape = c(15)
      ),
      order = 1
    ),
    shape = guide_legend(title = NULL)
  ) +

    labs(x = NULL, y = "District Total Population") +
  theme(
    axis.title.x = element_blank(),
    axis.text.x = element_blank(),
    axis.ticks.x = element_blank(),
    legend.margin = margin(5, 5, 5, 5),
    legend.spacing.y = unit(0, "pt"),
    legend.title = element_text(margin = margin(1, 0, 3, 0))
  )
# ggsave("../../diss/classicthesis/gfx/pops-by-distr.pdf", width = 7, height = 3)

# Square vote share by district
ggplot(
  master,
  aes(distr,
    sqre_share,
    group = distr,
    fill = distr,
    shape = type
  )
) +
  geom_boxplot(show.legend = FALSE) +
  geom_point(data = gerry, size = 6, colour = "grey30") +
  geom_point(data = gerry, size = 4, colour = "white") +
  scale_shape_manual(name = NULL, values = c(16)) +
  scale_fill_manual(name = "District", values = c(
    "#63C2A9",
    "#FD8C62",
    "#8E9FCC",
    "#E889C3",
    "#A7D855",
    "#FFD930"
  )) +
  guides(fill = guide_legend(
    override.aes = list(
      size = 6,
      colour = c(
        "#63C2A9",
        "#FD8C62",
        "#8E9FCC",
        "#E889C3",
        "#A7D855",
        "#FFD930"
      ),
      shape = c(15)
    ),
    order = 1
  )) +
  scale_y_continuous(label = percent, limits = c(0.4, 0.6)) +
  labs(x = "District", y = "Square Vote Share") +
  theme(
    axis.title.x = element_blank(),
    axis.text.x = element_blank(),
    axis.ticks.x = element_blank(),
    legend.margin = margin(5, 5, 5, 5),
    legend.spacing.y = unit(0, "pt"),
    legend.title = element_text(margin = margin(1, 0, 3, 0))
  )
# ggsave("../../diss/classicthesis/gfx/sqre-share-by-distr.pdf", width = 7, height = 3)


gerry_by_plan <- filter(by_plan, plan_label==9999)


filter(by_plan, plan_label != 9999) %>%
ggplot(aes(win_count, fill = distr_winner, colour = distr_winner)) +
  geom_histogram(binwidth = 1, show.legend = FALSE) + # , color = "#4C67A5", fill = "#D2D9EB") +
  geom_point(
      data = gerry_by_plan, 
      y = 0,
      size = 6, 
      colour = "grey30"
  ) +
  geom_point(
      data = gerry_by_plan, 
      y = 0,
      size = 3, 
      colour = "white"
  ) +
  geom_text(
    aes(label = comma(stat(count)), colour=distr_winner),
    stat = "count",
    vjust = -0.5,
    size = 5,
    show.legend = FALSE
  ) +
  facet_wrap(~distr_winner, labeller = labeller(distr_winner = parties)) +
  scale_color_manual(values = c("#4C67A5", "#F64805")) +
  scale_fill_manual(
      name = NULL, 
      values = c("#D2D9EB", "#FFD7C8"), 
      breaks = "circle", 
      labels = "gerry"
  ) +
  scale_y_continuous(trans='log10', limits=c(1,1200))+#, breaks=c(1,2,10,12,100,130,300, 750))+
  labs(x = "Number of Districts Won", y = "Win Count") +
  theme(
    legend.margin = margin(5, 5, 5, 5),
    legend.spacing.y = unit(0, "pt"),
    legend.title = element_text(margin = margin(1, 0, 3, 0))
  )
ggsave("../../diss/classicthesis/gfx/num-distrs-party-wins.pdf", width = 7, height = 3.8)

ggplot(
    filter(master, distr==1), 
    aes(reg2, colour = "#4C67A5", fill = "#D2D9EB")
) +
  geom_histogram(binwidth = 0.02) +
  geom_point(
      data = filter(master, type == "gerry"), 
      aes(x = reg2, y = 1, shape = "gerry"), 
      size = 5, colour = "gray30"
  ) +
  geom_point(
      data = filter(master, type == "gerry"),
      aes(x = reg2, y = 1, shape = "gerry"),
      size = 3, colour = "white"
  ) +
  annotate(geom='curve', x=-.5, y=180, xend=-0.69, yend=20, curvature=.22, arrow=arrow(length=unit(2,'mm')))+
  annotate(geom='text', x=-.488, y=186, label='-0.69', hjust='left', size=5)+
  guides(shape = guide_legend(title = NULL), color = FALSE, fill = FALSE) +
  scale_color_manual(values = c("#4C67A5")) +
  scale_fill_manual(values = c("#D2D9EB")) +
  labs(x = "Relative Efficiency Gap", y = "Count") +
  xlim(-0.75, 0.75)+
  theme(
    legend.spacing.y = unit(0, "pt"),
    legend.title = element_text(margin = margin(1, 0, 3, 0))
  )
ggsave("../../diss/classicthesis/gfx/rela-eff-gap.pdf", width = 7, height = 3.5)


hi_reg <- filter(master, reg2 > 0.6) #%>% distinct_at(vars(plan_label), .keep_all=TRUE)
write_csv(hi_reg, '../redist/logs/prod-run-hi-reg-plans.csv')
lo_reg <- filter(master, reg2 < -0.6) #%>% distinct_at(vars(plan_label), .keep_all=TRUE)
write_csv(lo_reg, '../redist/logs/prod-run-lo-reg-plans.csv')
tails <- filter(master, win_count>4)# %>% distinct_at(vars(plan_label), .keep_all=TRUE)
write_csv(tails, '../redist/logs/prod-run-lopsided-distr-wins-plans.csv')

filter(master, plan_label==710)

# Tabulate number of times x districts were won for squares across all plans
group_by(master, plan_label, distr_winner) %>%
  filter(distr_winner == "square", type != 'gerry') %>%
  summarise(n()) %>% 
  rename(distr_wins = 'n()') %>% 
  group_by(distr_wins) %>% 
  summarise(n())

# Archive

# ggplot(elect, aes(sqre_share, fill=distr)) +
#  geom_histogram(binwidth=0.01) +
#  facet_wrap(~distr)+
#  scale_fill_manual(name = "District", values = c("#63C2A9", "#FD8C62", "#8E9FCC", "#E889C3", "#A7D855", "#FFD930")) +
#  scale_x_continuous(label=percent)+
#  theme(
#    axis.text.x = element_text(angle = 45, vjust = .9, hjust = 0.9),
#  )



# ggplot(master, aes(distr, circ_marg, group = distr, fill = distr, shape = type)) +
#  geom_boxplot(show.legend = FALSE) +
#  geom_point(data = gerry, size = 6, colour = "grey30") +
#  geom_point(data = gerry, size = 4, colour = "white") +
#  scale_shape_manual(name = NULL, values = c(16)) +
#  scale_fill_manual(name = "District", values = c("#63C2A9",
#                                                  "#FD8C62",
#                                                  "#8E9FCC",
#                                                  "#E889C3",
#                                                  "#A7D855",
#                                                  "#FFD930")) +
#  guides(fill = guide_legend(override.aes = list(size = 6,
#                                                 colour = c("#63C2A9",
#                                                            "#FD8C62",
#                                                            "#8E9FCC",
#                                                            "#E889C3",
#                                                            "#A7D855",
#                                                            "#FFD930"),
#                                                            shape = c(15)),
#                                                            order = 1))+
#  scale_y_continuous(label=percent)+
#  labs(x=NULL, y="Circle Margin of Victory")+
#  theme(axis.title.x=element_blank(),
#        axis.text.x=element_blank(),
#        axis.ticks.x=element_blank(),
#        legend.margin = margin(5,5,5,5),
#        legend.spacing.y = unit(0, "pt"),
#        legend.title = element_text(margin = margin(1,0,3,0)))
# ggsave("../../diss/classicthesis/gfx/circ-margin-by-distr.pdf", width = 6, height = 4)
#
# ggplot(master, aes(distr, sqre_marg, group = distr, fill = distr, shape=type)) +
#  geom_boxplot(show.legend = FALSE) +
#  geom_point(data = gerry, size = 6, colour = "grey30") +
#  geom_point(data = gerry, size = 4, colour = "white") +
#  scale_shape_manual(name = NULL, values = c(16)) +
#  scale_fill_manual(name = "District", values = c("#63C2A9",
#                                                  "#FD8C62",
#                                                  "#8E9FCC",
#                                                  "#E889C3",
#                                                  "#A7D855",
#                                                  "#FFD930")) +
#  guides(fill = guide_legend(override.aes = list(size = 6,
#                                                 colour = c("#63C2A9",
#                                                            "#FD8C62",
#                                                            "#8E9FCC",
#                                                            "#E889C3",
#                                                            "#A7D855",
#                                                            "#FFD930"),
#                                                            shape = c(15)),
#                                                            order = 1))+
#  scale_y_continuous(label=percent)+
#  labs(x='District', y="Square Margin of Victory")
#  theme(axis.title.x=element_blank(),
#        axis.text.x=element_blank(),
#        axis.ticks.x=element_blank(),
#        legend.margin = margin(5,5,5,5),
#        legend.spacing.y = unit(0, "pt"),
#        legend.title = element_text(margin = margin(1,0,3,0)))
# ggsave("../../diss/classicthesis/gfx/sqre-margin-by-distr.pdf", width = 6, height = 4)

# District wins by party
#ggplot(elect, aes(distr, fill = distr, group = distr)) +
#  geom_bar() +
#  # geom_text(aes(label=scales::percent(..prop..)),
#  #  stat='count',
#  #  nudge_y=0.125,
#  #  vjust='-.5',
#  # )+
#  # geom_histogram(stat = "count") +
#  facet_wrap(~winner, labeller = labeller(winner = parties)) +
#  scale_fill_manual(name = "District", values = c("#63C2A9", "#FD8C62", "#8E9FCC", "#E889C3", "#A7D855", "#FFD930")) +
#  # scale_y_continuous(label=percent)+
#  labs(x = "District", y = "District Wins") +
#  theme(
#    axis.title.x = element_blank(),
#    axis.text.x = element_blank(),
#    axis.ticks.x = element_blank(),
#    legend.margin = margin(5, 5, 5, 5),
#    legend.spacing.y = unit(0, "pt"),
#    legend.title = element_text(margin = margin(1, 0, 3, 0))
#  )
# ggsave("../../diss/classicthesis/gfx/party-wins-by-distr.pdf", width = 7, height = 3)

# Circle vote share by district
#ggplot(master, aes(distr, circ_share, group = distr, fill = distr, shape = type)) +
#  geom_boxplot(show.legend = FALSE) +
#  geom_point(data = gerry, size = 6, colour = "grey30") +
#  geom_point(data = gerry, size = 4, colour = "white") +
#  scale_shape_manual(name = NULL, values = c(16)) +
#  scale_fill_manual(name = "District", values = c(
#    "#63C2A9",
#    "#FD8C62",
#    "#8E9FCC",
#    "#E889C3",
#    "#A7D855",
#    "#FFD930"
#  )) +
#  guides(fill = guide_legend(
#    override.aes = list(
#      size = 6,
#      colour = c(
#        "#63C2A9",
#        "#FD8C62",
#        "#8E9FCC",
#        "#E889C3",
#        "#A7D855",
#        "#FFD930"
#      ),
#      shape = c(15)
#    ),
#    order = 1
#  )) +
#  scale_y_continuous(label = percent, limits = c(0.4, 0.6)) +
#  labs(x = "District", y = "Circle Vote Share") +
#  theme(
#    axis.title.x = element_blank(),
#    axis.text.x = element_blank(),
#    axis.ticks.x = element_blank(),
#    legend.margin = margin(5, 5, 5, 5),
#    legend.spacing.y = unit(0, "pt"),
#    legend.title = element_text(margin = margin(1, 0, 3, 0))
#  )
# ggsave("../../diss/classicthesis/gfx/circ-share-by-distr.pdf", width = 7, height = 3)