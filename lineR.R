months <- c("January", "February", "March", "April", "May", "June", 
            "July", "August", "September", "October", "November", "December")
sales <- c(5000, 6000, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 9500, 9000, 10000)

plot(sales, type = "o", col = "blue", xlab = "Month", ylab = "Sales", main = "Monthly Sales Performance")
axis(1, at = 1:12, labels = months)
