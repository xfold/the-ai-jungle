# Using apyori library to learn association rules

> **Note**<br/>
**You can find the jupyter notebook [here](apyori.ipynb)**

**1. What are association rules?**

Association rules are a type of rule-based technique used in data mining and machine learning. They are used to identify interesting relationships or patterns in large datasets. Specifically, association rules find relationships between items in a transactional database or market basket data. These rules highlight the presence of specific combinations of items that frequently occur together in the data.

**Example:**
Let's consider a grocery store transaction database. An association rule might be: {Bread, Milk} → {Butter}. This rule suggests that customers who buy both Bread and Milk are likely to buy Butter as well.

**2. What are they used for?**

Association rules are primarily used for market basket analysis and recommendation systems. They help businesses understand customer behavior, discover item associations, and optimize product placement and promotions. By identifying co-occurrence patterns, businesses can make data-driven decisions to improve customer satisfaction, increase sales, and enhance marketing strategies.

**3. How can they be used, and what do you need?**

To use association rules, you need a transactional dataset where each transaction consists of items purchased together. This dataset is typically in the form of a binary matrix, where each row represents a transaction, and each column corresponds to an item, indicating whether the item was present in the transaction (1) or not (0). It can also be a dataset with a list of items bought together, as in this example.

To apply association rule mining, you can use algorithms like Apriori or FP-Growth. These algorithms take the transactional dataset as input and generate a set of association rules based on certain metrics like support, confidence, and lift.

**Example:**
Suppose you have a dataset containing customer purchase information, where each row represents a transaction, and the columns represent different products. Each cell contains 1 if the product was purchased in that transaction and 0 otherwise.

```
Transaction ID | Bread | Milk | Butter | Eggs | Cheese
1              | 1     | 1    | 0      | 1    | 0
2              | 1     | 0    | 1      | 1    | 0
3              | 0     | 1    | 1      | 0    | 1
... and so on
```

**4. How to select the best association rule once you have the results?**

After applying association rule mining algorithms, you will have a list of association rules along with their corresponding metrics like support, confidence, and lift. The selection of the best association rule depends on your specific objectives and requirements.

Here are some criteria you can use to select the best association rules:

- **Lift:** Choose rules with high lift values. Lift measures how much more likely items are bought together than if they were purchased independently. Higher lift values indicate stronger associations between items.

- **Confidence:** Consider rules with high confidence values. Confidence measures the likelihood that the "consequent" (right-hand side) of the rule is purchased given that the "antecedent" (left-hand side) is purchased. High confidence indicates a strong prediction power of the rule.

- **Support:** Look for rules with significant support values. Support measures the frequency of occurrence of both the antecedent and consequent together. Higher support values indicate that the rule applies to a considerable number of transactions.

- **Practicality:** Select rules that make sense from a business perspective and align with your goals. Sometimes, high-confidence rules may be too obvious to be actionable or may not provide valuable insights.

By considering these factors, you can choose the association rules that are most meaningful and relevant to your specific application.

**Example:**
Let's say you have generated several association rules from a market basket analysis. Among those rules, you might select the ones with a lift greater than 1.5, a confidence higher than 0.7, and a support greater than 0.05. These rules would indicate strong associations between items with a high likelihood of co-occurrence in customer transactions and are significant enough to be actionable for marketing strategies.