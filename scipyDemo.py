import scipy.stats as stats

x = stats.chi2.rvs(3, size=50)
y = 2.5 + 1.2 * x + stats.norm.rvs(size=50, loc=0, scale=1.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print("Slope of fitted model is:" , slope)
print("Intercept of fitted model is:", intercept)
print("R-squared:", r_value**2)