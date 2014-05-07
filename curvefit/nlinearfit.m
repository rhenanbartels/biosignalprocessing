%Create x and y values
xdata = linspace(0, 10, 200);
ydata = 10 + 15.*exp(-xdata / 2) + randn(1, length(xdata));

%Define the exponential model
my_fun = @(p) sum((ydata- (p(1) + p(2).*exp(-xdata / p(3)))).^2);

%Function to evaluate the model. In this case we need to provide the error
%funtion: error sum of squares
fun_eval = @(p, t) p(1) + p(2).*exp(-t / p(3));

%Inital guesses
p0 = [min(ydata), max(ydata) - min(ydata), xdata(end) / 3]

%Nonlinear fit
result = fminsearch(my_fun, p0);

plot(xdata, ydata, 'k.')
hold on
plot(xdata, fun_eval(result, xdata), 'r')
xlabel('Time (s)')
ylabel('Signal')
