#  Load some libraries and ancillary bits
library(tidyverse)
# library(forcats)
# library(lubridate)
# library(scales)
library(extrafont)
library(extrafontdb)
loadfonts()
fonts()

# Set up look and feel of ggplots
theme_update(
  text = element_text(family = "Source Sans Pro"),
  plot.title = element_text(size = 18),
  plot.subtitle = element_text(size = 14),
  plot.margin = margin(5, 60, 5, 5),
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
elect <- read_csv("../redist/elections/1mil-iters-exp-graph.csv",
  col_names = c("index", "plan_id", "plan_label", "distr", "vote_circ", "vote_sqre", "total"),
  col_types = "idifiii",
  skip = 1
)

elect <- mutate(elect, circ_marg = (vote_circ / total - vote_sqre / total) * 100, sqre_marg = (vote_sqre / total - vote_circ / total) * 100)
elect <- mutate(elect, winner = ifelse(circ_marg > sqre_marg,'circle', 'square'))

  
ggplot(elect, aes(total))+geom_histogram(binwidth = 1)

ggplot(elect, aes(distr, total, group = distr, fill = distr)) +
  geom_boxplot() +
  scale_fill_manual(name='District', values = c("#46AC90", "#FA6A34", "#6981BA", "#DF5EAE", "#89BF2B", "#E6BC00"))

ggplot(elect, aes(distr, circ_marg, group = distr, fill = distr)) +
  geom_boxplot()+
  scale_fill_manual(name='District', values = c("#46AC90", "#FA6A34", "#6981BA", "#DF5EAE", "#89BF2B", "#E6BC00"))

ggplot(elect, aes(distr, sqre_marg, group = distr, fill = distr)) +
  geom_boxplot()+
  scale_fill_manual(name='District', values = c("#46AC90", "#FA6A34", "#6981BA", "#DF5EAE", "#89BF2B", "#E6BC00"))

distrs = group_by(elect, distr)  
win_count_by_plan = group_by(elect, plan_label) %>% count(winner)

ggplot(distrs, aes(distr))+geom_histogram(stat='count')+facet_wrap(~winner)

ggplot(win_count_by_plan, aes(n))+geom_histogram(binwidth = 1)+facet_wrap(~winner)


# fte <- mutate(fte,
#              election_date = as.Date(election_date,
#                                      format = "%d/%m/%Y"),
#              startdate = as.Date(startdate,
#                                  format = "%d/%m/%Y"),
#              enddate = as.Date(enddate,
#                                format = "%d/%m/%Y")
# )
#
## Define some constants and data frames
# swing_sts <- c("MI", "NH", "PA", "WI", "FL", "MN")
#
# nat_polls <- fte %>% filter(location_abv == "US")
# st_polls <- fte %>% filter(location_abv != "US" & location_abv != "DC")
# swing_polls <- fte %>% filter(location_abv %in% swing_sts)
#
# sept_st_polls <- st_polls %>% filter(enddate > as.Date("2016-09-01"))
# sept_nat_polls <- nat_polls %>% filter(enddate > as.Date("2016-09-01"))
# sept_swing_polls <- swing_polls %>% filter(enddate > as.Date("2016-09-01"))
#
## Summarise national pollsters by rating
# poll_rtgs <- nat_polls %>%
#  group_by(pollster, rating) %>%
#  summarise(count = n())
#
# st_poll_rtgs <- st_polls %>%
#  group_by(pollster, rating) %>%
#  summarise(count = n())
#
# a <- st_poll_rtgs %>% filter(rating == "A")
# b <- st_poll_rtgs %>% filter(rating == "B")
# c <- st_poll_rtgs %>% filter(rating == "C")
# quantile(a$count)
# quantile(b$count)
# quantile(c$count)
#
## Pollster ratings histograms and box plots; state and national
# ggplot(poll_rtgs, aes(rating, fill = rating)) +
#  geom_bar(colour = "black") +
#  geom_text(
#    aes(label = stat(count)),
#    stat = "count",
#    vjust = 2.0,
#    colour = "black",
#    size = 5
#  ) +
#  theme(
#    legend.position = "none",
#    axis.title.y = element_text(margin = margin(0, 0, 0, 0)),
#    plot.margin = margin(5, 50, 5, 5),
#    plot.title = element_text(size = 16)
#  ) +
#  labs(title = "National Pollsters per\nRating Category",
#       x = "Rating",
#       y = "Count")
# ggsave("../report/imgs/nat-pollsters-per-cat.pdf", width = 3.5, height = 4)
#
# ggplot(st_poll_rtgs, aes(rating, fill = rating)) +
#  geom_bar(colour = "black") +
#  geom_text(
#    aes(label = stat(count)),
#    stat = "count",
#    vjust = 2.0,
#    colour = "black",
#    size = 5
#  ) +
#  theme(
#    legend.position = "none",
#    axis.title.y = element_text(margin = margin(0, 0, 0, 0)),
#    plot.margin = margin(5, 40, 5, 5),
#    plot.title = element_text(size = 16)
#  ) +
#  labs(title = "State Pollsters per\nRating Category",
#       x = "Rating",
#       y = "Count")
# ggsave("../report/imgs/st-pollsters-per-cat.pdf", width = 3.5, height = 4)
#
# ggplot(poll_rtgs, aes(rating, count, fill = rating)) +
#  geom_boxplot() +
#  scale_y_continuous(trans = "log10", limits = c(1, 1000)) +
#  theme(
#    legend.position = "none",
#    axis.title.y = element_text(margin = margin(0, 0, 0, 0)),
#    plot.margin = margin(5, 60, 5, 5),
#    plot.title = element_text(size = 16)
#  ) +
#  labs(title = "National Polls\nConducted per\nPollster",
#       x = "Rating",
#       y = "Count")
# ggsave("../report/imgs/nat-polls-per-cat-box.pdf", width = 3.5, height = 4)
#
# ggplot(st_poll_rtgs, aes(rating, count, fill = rating)) +
#  geom_boxplot() +
#  scale_y_continuous(trans = "log10", limits = c(1, 1000)) +
#  theme(
#    legend.position = "none",
#    axis.title.y = element_text(margin = margin(0, 0, 0, 0)),
#    plot.margin = margin(5, 40, 5, 5)
#  ) +
#  labs(title = "State Polls\nConducted per\nPollster",
#       x = "Rating",
#       y = "Count")
# ggsave("../report/imgs/st-polls-per-cat-box.pdf", width = 3.5, height = 4)
#
#
# ggplot(nat_polls, aes(rating, fill = rating)) +
#  geom_bar(colour = "black") +
#  geom_text(
#    aes(label = stat(count)),
#    stat = "count",
#    vjust = 2.0,
#    colour = "black",
#    size = 5
#  ) +
#  theme(
#    legend.position = "none",
#    axis.title.y = element_text(margin = margin(0, 0, 0, 0)),
#    plot.margin = margin(5, 60, 5, 5),
#    plot.title = element_text(size = 16)
#  ) +
#  labs(title = "National Polls per\nRating Category",
#       x = "Rating",
#       y = "Count") +
#  theme(legend.position = "none")
# ggsave("../report/imgs/nat-polls-per-cat.pdf", width = 3.5, height = 4)
#
# ggplot(st_polls, aes(rating, fill = rating)) +
#  geom_bar(colour = "black") +
#  geom_text(
#    aes(label = stat(count)),
#    stat = "count",
#    vjust = 2.0,
#    colour = "black",
#    size = 5
#  ) +
#  theme  (
#    legend.position = "none",
#    axis.title.y = element_text(margin = margin(0, 0, 0, 0)),
#    plot.margin = margin(5, 60, 5, 5),
#    plot.title = element_text(size = 16)
#  ) +
#  labs(title = "State Polls per\nRating Category",
#       x = "Rating",
#       y = "Count") +
#  theme(legend.position = "none")
# ggsave("../report/imgs/st-polls-per-cat.pdf", width = 3.5, height = 4)
#
## Calculate error (absolute value of margin_poll - margin_actual) against time
# error_by_week <- nat_polls %>%
#  group_by(week = floor_date(enddate, "week"), rating) %>%
#  summarise(med_error = median(error))
#
# after_june <- filter(error_by_week, week > as.Date("2016-06-01"))
#
# ggplot(after_june, aes(week, med_error, colour = rating)) +
#  geom_point(alpha = 0.5) +
#  geom_line(alpha = 0.3) +
#  geom_smooth(method = "lm", se = FALSE) +
#  scale_x_date(date_breaks = "2 weeks", date_labels = "%e %b") +
#  theme(
#    axis.text.x = element_text(angle = 45, vjust = .9, hjust = 0.9),
#    axis.title.x = element_blank(),
#    legend.position = c(1.0, 1.0),
#    plot.margin = margin(5, 50, -5, 5),
#    legend.justification = c(1.1, 1.1)
#  ) +
#  labs(
#    title = "Weekly Median Polling Error Over Time",
#    subtitle = "National Polls Grouped by Pollster Rating",
#    x = "Date of Poll",
#    y = "Weekly Median Polling Error",
#    colour = "Pollster\nRating"
#  )
# ggsave("../report/imgs/polls-over-time.pdf", width = 8, height = 4.5)
#
## Compute plot of poll_wt over time
# ggplot(fte, aes(enddate, poll_wt, colour = rating)) +
#  geom_point() +
#  facet_wrap(~rating) +
#  scale_x_date(
#    date_labels = "%e %b",
#    breaks = as.Date(c("2016-07-01",
#                       "2016-08-01",
#                       "2016-09-01",
#                       "2016-10-01",
#                       "2016-11-01")),
#    limits = as.Date(c("2016-06-01", "2016-11-08"))
#  ) +
#  labs(title = "Poll Weight over Time by Rating", y = "Poll Weight") +
#  theme(
#    legend.position = "none",
#    plot.margin = margin(5, 50, -8, 5),
#    axis.text.x = element_text(angle = 45, vjust = .9, hjust = 0.9),
#    axis.title.x = element_blank()
#  )
# ggsave("../report/imgs/poll-weight.pdf", width = 8, height = 3.5)
#
## Plot vote margin by state
# marg_by_loc <- fte %>%
#  filter(location_abv != "DC" & margin_actual > -10 & margin_actual < 10) %>%
#  group_by(margin_actual, location) %>%
#  summarise()
# marg_levels <- marg_by_loc$location
# marg_by_loc <- mutate(marg_by_loc,
#                      location = factor(location, levels = marg_levels))
#
# ggplot(marg_by_loc, aes(margin_actual,
#  fct_relevel(location, c("U.S.")),
#  fill = margin_actual
# )) +
#  geom_vline(xintercept = 0, alpha = .6) +
#  geom_vline(xintercept = -2, alpha = .4) +
#  geom_vline(xintercept = 2, alpha = .4) +
#  geom_vline(xintercept = -5, alpha = .2) +
#  geom_vline(xintercept = 5, alpha = .2) +
#  geom_point(size = 6, colour = "black", pch = 21) +
#  labs(title = "Margin of Victory by State",
#       x = "Margin of Victory (%)",
#       y = "State") +
#  scale_x_continuous(
#    breaks = c(-10, -5, -2, 0, 2, 5, 10),
#    labels = c("10", "5", "2", "0", "2", "5", "10"),
#    limits = c(-10, 10)
#  ) +
#  scale_fill_gradient2(
#    low = "red", mid = "white", high = "blue",
#    name = "Margin",
#    breaks = c(-8, 0, 8),
#    labels = c(
#      "For Trump",
#      "Neutral",
#      "For Clinton"
#    )
#  ) +
#  theme(
#    axis.text.x = element_text(size = 14),
#    axis.text.y = element_text(
#      margin = margin(40, 5, 40, 5),
#      size = 14
#    ),
#    plot.margin = margin(10, 150, 10, 10),
#    legend.position = c(0.99, 0.01),
#    legend.justification = c(1.0, 0.0)
#  )
# ggsave("../report/imgs/margin-of-victory.pdf", width = 9, height = 6)
#
## Plot swing state error and poll counts by rating
# ggplot(sept_swing_polls, aes(rating, error, fill = rating)) +
#  geom_boxplot() +
#  facet_wrap(~location, dir = "v") +
#  ylim(0, 20) +
#  labs(
#    title = "Distributions of Error\nfor Polls after Sept.",
#    x = "Rating",
#    y = "Polling Error"
#  ) +
#  theme(legend.position = "none")
# ggsave("../report/imgs/swing-error.pdf", width = 5, height = 8)
# ggplot(sept_swing_polls, aes(rating, fill = rating)) +
#  geom_histogram(stat = "count", colour = "black") +
#  geom_text(
#    aes(label = stat(count)),
#    stat = "count",
#    vjust = 1.5,
#    colour = "black",
#    size = 5
#  ) +
#  facet_wrap(~location, dir = "v") +
#  labs(
#    title = "Number of Polls\nafter Sept.",
#    x = "Rating",
#    y = "Count"
#  ) +
#  theme(legend.position = "none")
# ggsave("../report/imgs/swing-counts.pdf", width = 5, height = 8)
#
## Plot error by poll rating, for swing states (less than %5 margin)
## and nationally
# ggplot(filter(sept_st_polls, abs(margin_actual) < 5),
#       aes(rating, error, fill = rating)) +
#  geom_boxplot() +
#  ylim(0, 20) +
#  labs(
#    title = "Aggregate Error of\nSwing State Polls after Sept.",
#    x = "Rating",
#    y = "Polling Error"
#  ) +
#  theme(legend.position = "none")
# ggsave("../report/imgs/swing-error-agg.pdf", width = 5, height = 5)
# ggplot(sept_nat_polls, aes(rating, error, fill = rating)) +
#  geom_boxplot() +
#  ylim(0, 20) +
#  labs(
#    title = "Error of National\nPolls after Sept.",
#    x = "Rating",
#    y = "Polling Error"
#  ) +
#  theme(legend.position = "none")
# ggsave("../report/imgs/nat-error-sept.pdf", width = 5, height = 5)
#
## Compute some stats
# median(sept_nat_polls$error)
# median(sept_st_polls$error)
#
