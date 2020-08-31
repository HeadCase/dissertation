library(tidyverse)
library(showtext)
library(scales)
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

log1 <- read_csv("../redist/logs/4mil-const-pt0025-ban-ncontig-variance-fixed-distr1-1.csv")
log2 <- read_csv("../redist/logs/4mil-const-pt0025-ban-ncontig-variance-fixed-distr1-2.csv")
log3 <- read_csv("../redist/logs/4mil-const-pt0025-ban-ncontig-variance-fixed-distr1-3.csv")
log4 <- read_csv("../redist/logs/4mil-const-pt0025-ban-ncontig-variance-fixed-distr1-4.csv")
log5 <- read_csv("../redist/logs/4mil-const-pt0025-ban-ncontig-variance-fixed-distr1-5.csv")
log6 <- read_csv("../redist/logs/4mil-const-pt0025-ban-ncontig-variance-fixed-distr1-6.csv")
log7 <- read_csv("../redist/logs/4mil-const-pt0025-ban-ncontig-variance-fixed-distr1-7.csv")
log8 <- read_csv("../redist/logs/4mil-const-pt0025-ban-ncontig-variance-fixed-distr1-8.csv")

master <- bind_rows(log1,log2,log3,log4,log5,log6,log7,log8)

subm <- slice_head(master, n=1000000)

ggplot(master, aes(outcome, fill=outcome, colour=outcome))+
  geom_histogram(stat='count', show.legend = FALSE)+
  geom_text(
    aes(label = comma(stat(count)), colour=outcome),
    stat = "count",
    vjust = -0.8,
    size = 5,
    show.legend = FALSE
  ) +
  scale_fill_manual(values=c('#BCE17F', '#FEB296', '#AFBBDA'))+
  scale_colour_manual(values=c('#74A225', '#F64805', '#4C67A5'))+
  scale_y_continuous(labels=label_comma(), limits = c(0,3000000))+
  labs(x='Outcome', y='Count')+
  theme(
    plot.margin = margin(5, 100, 5, 5),
  )
ggsave("../../diss/classicthesis/gfx/accept-reject-repeat.pdf", width = 7, height = 4)
  
