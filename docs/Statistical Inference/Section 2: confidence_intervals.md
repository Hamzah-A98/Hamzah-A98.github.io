# Confidence Intervals

In a previous section (link), we learned that $\overline{X}$ is a consistent/trustworthy estimate of $\mu$. If $n$ is "large", CLT states that 
$$ \bar{X} \sim N(\mu, \frac{\sigma^{2}}{n}) \label{clt} \tag{1}$$

$\textbf{Question}$: How can we take advantage of the Central Limit Theorem to learn more about our parameter of interest, $\mu$? Can we construct a range of values that is **likely** to contain $\mu$? 

Based on our distribution result, we can standardize \eqref{clt}: 

$$ \frac{\overline{X} - \mu}{\sigma/n} \sim N(0, 1)$$

Here, $\frac{\overline{X} - \mu}{\sigma/n}$ is a random variable whose distribution does not depend on $\mu$ or $\sigma$. This is referred to as a pivotal quantity. 