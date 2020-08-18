#  Load some libraries and ancillary bits
library(tidyverse)
library(showtext)
# library(forcats)
# library(lubridate)
library(scales)
# library(extrafont)
# library(extrafontdb)
#
# font_import()
# loadfonts()
# fonts()
font_add(family = "Source Sans Pro", regular = "~/CloudStation/home/docs/fonts/Adobe CC/Source Sans Pro Regular.otf")

showtext_auto()

# Set up look and feel of ggplots
theme_update(
  text = element_text(family = "Source Sans Pro"),
  plot.title = element_text(size = 18),
  plot.subtitle = element_text(size = 14),
  plot.margin = margin(5, 10, 5, 35),
  axis.text = element_text(size = 14),
  axis.title.x = element_text(margin = margin(10, 0, 0, 0)),
  axis.title.y = element_text(margin = margin(0, 10, 0, 0)),
  axis.text.y = element_text(margin = margin(5, 5, 5, 5)),
  axis.text.x = element_text(margin = margin(5, 5, 5, 5)),
  axis.title = element_text(size = 14),
  strip.text = element_text(size = 12),
  legend.text = element_text(size = 14),
  legend.title = element_text(size = 14),
  legend.background = element_rect(colour = "darkgrey", fill = "white"),
  legend.key = element_rect(
    colour = "transparent",
    fill = "transparent"
  ),
)
# hex_codes1 <- hue_pal()(12)                             # Identify hex codes
# show_col(hex_codes1)

# Read in data
elect <- read_csv("../redist/elections/4mil-const-pt0025-ban-ncontig-variance-fixed-distr1.csv",
  col_names = c("index", "plan_id", "plan_label", "distr", "vote_circ", "vote_sqre", "total"),
  col_types = "idifiii",
  skip = 1
)

elect <- mutate(elect, circ_share = (vote_circ / total), sqre_share = (vote_sqre / total))
elect <- mutate(elect, circ_marg = circ_share - sqre_share, sqre_marg = sqre_share - circ_share)
elect <- mutate(elect, winner = ifelse(circ_marg > sqre_marg, "circle", "square"))
elect <- mutate(elect, type = "simulated")

gerry <- read_csv("../redist/elections/gerrymandered-plan.csv",
  col_names = c("index", "plan_id", "plan_label", "distr", "vote_circ", "vote_sqre", "total"),
  col_types = "idifiii",
  skip = 1
)

gerry <- mutate(gerry, circ_share = (vote_circ / total), sqre_share = (vote_sqre / total))
gerry <- mutate(gerry, circ_marg = circ_share - sqre_share, sqre_marg = sqre_share - circ_share)
gerry <- mutate(gerry, winner = ifelse(circ_marg > sqre_marg, "circle", "square"))
gerry <- mutate(gerry, type = "gerry")

master <- bind_rows(elect, gerry)

parties <- c(circle = "Circle Party", square = "Square Party")

# ggplot(elect, aes(total)) + geom_histogram(binwidth = 1, color = "#4C67A5", fill = "#D2D9EB")
# ggsave("../../diss/classicthesis/gfx/total-pop-hist.pdf", width = 6, height = 4)

type_split <- group_by(master, type)

ggplot(master, aes(distr, total, group = distr, fill = distr, shape = type)) +
  geom_boxplot(show.legend = FALSE) +
  geom_point(data = gerry, size = 6, colour = "grey30") +
  geom_point(data = gerry, size = 3, colour = "white") +
  scale_shape_manual(values = c(16)) +
  scale_fill_manual(name = "District", values = c("#63C2A9", 
                                                  "#FD8C62", 
                                                  "#8E9FCC", 
                                                  "#E889C3", 
                                                  "#A7D855", 
                                                  "#FFD930")) +
  guides(fill = guide_legend(override.aes = list(size = 6, 
                                                 colour = c("#63C2A9", 
                                                 "#FD8C62", 
                                                 "#8E9FCC", 
                                                 "#E889C3", 
                                                 "#A7D855", 
                                                 "#FFD930"), 
                                                 shape = c(15)), 
                                                 order = 1),
         shape = guide_legend(title=NULL))+
  labs(x=NULL,y='District Total Population')+
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank(),
        legend.margin = margin(5,5,5,5),
        legend.spacing.y = unit(0, "pt"),
        legend.title = element_text(margin = margin(1,0,3,0)))
ggsave("../../diss/classicthesis/gfx/pops-by-distr.pdf", width = 7, height = 3)

#ggplot(master, aes(distr, circ_marg, group = distr, fill = distr, shape = type)) +
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
#ggsave("../../diss/classicthesis/gfx/circ-margin-by-distr.pdf", width = 6, height = 4)
#
#ggplot(master, aes(distr, sqre_marg, group = distr, fill = distr, shape=type)) +
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

ggplot(master, aes(distr, circ_share, group = distr, fill = distr, shape=type)) +
  geom_boxplot(show.legend = FALSE) +
  geom_point(data = gerry, size = 6, colour = "grey30") +
  geom_point(data = gerry, size = 4, colour = "white") +
  scale_shape_manual(name = NULL, values = c(16)) +
  scale_fill_manual(name = "District", values = c("#63C2A9", 
                                                  "#FD8C62", 
                                                  "#8E9FCC", 
                                                  "#E889C3", 
                                                  "#A7D855", 
                                                  "#FFD930")) +
  guides(fill = guide_legend(override.aes = list(size = 6, 
                                                 colour = c("#63C2A9", 
                                                            "#FD8C62", 
                                                            "#8E9FCC", 
                                                            "#E889C3", 
                                                            "#A7D855", 
                                                            "#FFD930"), 
                                                            shape = c(15)), 
                                                            order = 1))+
  scale_y_continuous(label=percent, limits = c(0.4, 0.6))+
  labs(x='District', y="Circle Vote Share")+
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank(),
        legend.margin = margin(5,5,5,5),
        legend.spacing.y = unit(0, "pt"),
        legend.title = element_text(margin = margin(1,0,3,0)))
ggsave("../../diss/classicthesis/gfx/circ-share-by-distr.pdf", width = 7, height = 3)

ggplot(master, aes(distr, sqre_share, group = distr, fill = distr, shape=type)) +
  geom_boxplot(show.legend = FALSE) +
  geom_point(data = gerry, size = 6, colour = "grey30") +
  geom_point(data = gerry, size = 4, colour = "white") +
  scale_shape_manual(name = NULL, values = c(16)) +
  scale_fill_manual(name = "District", values = c("#63C2A9", 
                                                  "#FD8C62", 
                                                  "#8E9FCC", 
                                                  "#E889C3", 
                                                  "#A7D855", 
                                                  "#FFD930")) +
  guides(fill = guide_legend(override.aes = list(size = 6, 
                                                 colour = c("#63C2A9", 
                                                            "#FD8C62", 
                                                            "#8E9FCC", 
                                                            "#E889C3", 
                                                            "#A7D855", 
                                                            "#FFD930"), 
                                                            shape = c(15)), 
                                                            order = 1))+
  scale_y_continuous(label=percent, limits = c(0.4, 0.6))+
  labs(x='District', y="Square Vote Share")+
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank(),
        legend.margin = margin(5,5,5,5),
        legend.spacing.y = unit(0, "pt"),
        legend.title = element_text(margin = margin(1,0,3,0)))
ggsave("../../diss/classicthesis/gfx/sqre-share-by-distr.pdf", width = 7, height = 3)

distrs <- group_by(elect, distr)
win_count_by_plan <- group_by(elect, plan_label) %>% count(winner)
gerry_win_count_by_plan <- 
  group_by(gerry, plan_label) %>% count(winner)
win_count_by_distr <- group_by(elect, distr) %>% count(winner)
group_by(elect,distr)

ggplot(elect, aes(distr, fill=distr, group=distr)) +
  geom_bar() +
  #geom_text(aes(label=scales::percent(..prop..)),
  #  stat='count',
  #  nudge_y=0.125,
  #  vjust='-.5',
  #)+
  # geom_histogram(stat = "count") +
  facet_wrap(~winner, labeller = labeller(winner = parties)) +
  scale_fill_manual(name = "District", values = c("#63C2A9", "#FD8C62", "#8E9FCC", "#E889C3", "#A7D855", "#FFD930")) +
  #scale_y_continuous(label=percent)+
  labs(x='District', y="District Wins")+
  theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank(),
        legend.margin = margin(5,5,5,5),
        legend.spacing.y = unit(0, "pt"),
        legend.title = element_text(margin = margin(1,0,3,0)))
ggsave("../../diss/classicthesis/gfx/party-wins-by-distr.pdf", width = 7, height = 3)

ggplot(win_count_by_plan, aes(n, fill=winner, colour=winner)) +
  geom_histogram(binwidth = 1, show.legend = FALSE)+#, color = "#4C67A5", fill = "#D2D9EB") +
  geom_point(data=gerry_win_count_by_plan, y=40, size = 6, colour = "grey30")+
  geom_point(data=gerry_win_count_by_plan, y=40, size = 3, colour = "white")+
  facet_wrap(~winner, labeller = labeller(winner = parties))+
  scale_color_manual(values=c("#4C67A5", "#F64805"))+
  scale_fill_manual(name=NULL,values=c("#D2D9EB", "#FFD7C8"),breaks='circle', labels='Gerry')+
  labs(x='Number of Districts Won', y='Win Count')+
  theme(#legend.position = 'none',
        legend.margin = margin(5,5,5,5),
        legend.spacing.y = unit(0, "pt"),
        legend.title = element_text(margin = margin(1,0,3,0)))
ggsave("../../diss/classicthesis/gfx/num-distrs-party-wins.pdf", width = 7, height = 3)

ggplot(elect, aes(sqre_share, fill=distr)) +
  geom_histogram(binwidth=0.01) +
  facet_wrap(~distr)+
  scale_fill_manual(name = "District", values = c("#63C2A9", "#FD8C62", "#8E9FCC", "#E889C3", "#A7D855", "#FFD930")) +
  scale_x_continuous(label=percent)+
  theme(
    axis.text.x = element_text(angle = 45, vjust = .9, hjust = 0.9),
  )
ggplot(elect, aes(sqre_share)) +
  geom_histogram(binwidth = 1)
