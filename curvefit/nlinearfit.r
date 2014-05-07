#Create the x and y values
xdata <- seq(1, 10, by=1 / 100)
ydata <- 10 + 15 * exp(-xdata / 2) + rnorm(length(xdata))

#Create a data frame
data_frame <- data.frame(xdata=xdata, ydata=ydata)

#Model
myfun <- function(time, b1, b2, b3){
    b1 + b2 * exp(-time / b3)
}

#Inital guesses
p0 <- list(b1=min(ydata), b2=max(ydata) - min(ydata),b3=tail(xdata, n=1) / 3)

#Nonlinear fit
result <- nls(ydata ~ myfun(xdata, b1, b2, b3), data=data_frame, start=p0)

#Plot the curves
plot(xdata, ydata, xlab="Time (s)", ylab="Signal")
lines(xdata, predict(result, list(xdata)), lwd=3, col="red")


