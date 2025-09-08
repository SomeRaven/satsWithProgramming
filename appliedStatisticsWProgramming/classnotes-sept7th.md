# Variability in a Data Set

## Variance:

Standard Deviation = sqrt(Var(X)):
Where: 
    n=number samples
    x_bar=mean 

## Sample vs Population Spread

- sample variance formula: s^2 = E(xi - mean)^2 / (n-1)
- n - 1 in denominator gives unbiased estimate of population variance
- Use sample statistics to estimate population parameters.
- population sd: np.std(data)
- sample sd: np.std(data, ddof=1)

## Skewness
<img src="Screenshot 2025-09-08 at 1.53.36 PM (2).png" width="50%" >

## Summary Table:
|Name  | About  |
|------|--------|
|Mean  | Arthmetic center, sensitive to outliers. | 
|Median| Middle value, robust to outliers. | 
|Mode  | Most Frequent value, robuts. |
|Range | Max - Min, sensitive to outliers. | 
|IQR   | Spread of central 50%c, robust.  | 
|Variance & SD | Average deviation, sensitive | 

## Why it matters

- **System latency:** Meduan response time more reliable for SLA reporting
- **File sizes:** Skewed distributions, median gives typical value. 
- **Login attempts:** Outliers may indicate security issues. 
- **Server performance:** Use IQR/SD to compare variablilty across regions. 

