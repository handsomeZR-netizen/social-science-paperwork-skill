# Starter survey analysis script.
# Copy this file into the project, then edit DATA_PATH and construct item groups.

DATA_PATH <- "survey.csv"

required_packages <- c("readr", "dplyr", "tidyr", "psych", "ggplot2")
missing_packages <- required_packages[!vapply(required_packages, requireNamespace, logical(1), quietly = TRUE)]
if (length(missing_packages) > 0) {
  stop("Install required packages first: ", paste(missing_packages, collapse = ", "))
}

library(readr)
library(dplyr)
library(tidyr)
library(psych)
library(ggplot2)

survey <- read_csv(DATA_PATH, show_col_types = FALSE)

# Basic structure and missingness
print(glimpse(survey))
missing_summary <- survey %>%
  summarise(across(everything(), ~ sum(is.na(.x)))) %>%
  pivot_longer(everything(), names_to = "variable", values_to = "missing_n")
print(missing_summary)

# Example: reverse coding on a 1-5 scale.
# survey <- survey %>% mutate(item_03_r = 6 - item_03)

# Example: scale score. Replace item names with real questionnaire columns.
# craft_identity_items <- c("ci_01", "ci_02", "ci_03")
# print(psych::alpha(survey[craft_identity_items]))
# survey <- survey %>%
#   mutate(craft_identity = rowMeans(across(all_of(craft_identity_items)), na.rm = TRUE))

# Descriptive statistics for numeric variables
numeric_vars <- survey %>% select(where(is.numeric))
print(psych::describe(numeric_vars))

# Example regression. Replace outcome and predictors with theory-grounded variables.
# model <- lm(outcome ~ craft_identity + design_experience + age, data = survey)
# summary(model)
