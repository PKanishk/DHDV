categories <- c('Rent', 'Groceries', 'Utilities', 'Entertainment')
expenses <- c(30, 25, 20, 25)
pie(expenses, labels = categories, col = rainbow(length(categories)),
    main = "Household Expenses Distribution")