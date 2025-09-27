import pandas as pd
import numpy as np

# load datasets
diamonds = pd.read_csv("CSVS/diamonds.csv")
heart = pd.read_csv("CSVS/heart (5).csv")
loan = pd.read_csv("CSVS/loan_approval-1.csv")

print("PROBLEM 1: DIAMONDS DATASET")
print("="*50)

# basic info about diamonds dataset
print("Dataset shape:", diamonds.shape)
print("\nFirst few rows:")
print(diamonds.head())

print("\nCut distribution:")
print(diamonds['cut'].value_counts())

print("\nClarity distribution:")
print(diamonds['clarity'].value_counts())

print("\nColor distribution:")
print(diamonds['color'].value_counts())

# 1a. Probability of IDEAL cut
total_diamonds = len(diamonds)
ideal_diamonds = len(diamonds[diamonds['cut'] == 'Ideal'])
prob_ideal = ideal_diamonds / total_diamonds

print(f"\n1a. Probability of IDEAL cut:")
print(f"Total diamonds: {total_diamonds}")
print(f"IDEAL diamonds: {ideal_diamonds}")
print(f"P(IDEAL) = {ideal_diamonds}/{total_diamonds} = {prob_ideal:.4f}")

# 1b. Probability of VS1 clarity
vs1_diamonds = len(diamonds[diamonds['clarity'] == 'VS1'])
prob_vs1 = vs1_diamonds / total_diamonds

print(f"\n1b. Probability of VS1 clarity:")
print(f"VS1 diamonds: {vs1_diamonds}")
print(f"P(VS1) = {vs1_diamonds}/{total_diamonds} = {prob_vs1:.4f}")

# 1c. Probability of PREMIUM and color E
premium_e_diamonds = len(diamonds[(diamonds['cut'] == 'Premium') & (diamonds['color'] == 'E')])
prob_premium_e = premium_e_diamonds / total_diamonds

print(f"\n1c. Probability of PREMIUM and color E:")
print(f"PREMIUM and E diamonds: {premium_e_diamonds}")
print(f"P(PREMIUM and E) = {premium_e_diamonds}/{total_diamonds} = {prob_premium_e:.4f}")

# 1d. Probability of IDEAL or VS1 clarity
# P(A or B) = P(A) + P(B) - P(A and B)
ideal_vs1_diamonds = len(diamonds[(diamonds['cut'] == 'Ideal') & (diamonds['clarity'] == 'VS1')])
prob_ideal_or_vs1 = prob_ideal + prob_vs1 - (ideal_vs1_diamonds / total_diamonds)

print(f"\n1d. Probability of IDEAL or VS1:")
print(f"IDEAL and VS1 diamonds: {ideal_vs1_diamonds}")
print(f"P(IDEAL or VS1) = P(IDEAL) + P(VS1) - P(IDEAL and VS1)")
print(f"P(IDEAL or VS1) = {prob_ideal:.4f} + {prob_vs1:.4f} - {ideal_vs1_diamonds/total_diamonds:.4f} = {prob_ideal_or_vs1:.4f}")

print("\n" + "="*50)
print("PROBLEM 2: HEART DATASET")
print("="*50)

print("Dataset shape:", heart.shape)
print("\nFirst few rows:")
print(heart.head())

print("\nSex distribution (1=male, 0=female):")
print(heart['sex'].value_counts())

print("\nFasting blood sugar distribution (1=fbs>120, 0=fbs<=120):")
print(heart['fbs'].value_counts())

# 2i. P(fasting sugar > 120 | male)
males = heart[heart['sex'] == 1]
males_high_fbs = heart[(heart['sex'] == 1) & (heart['fbs'] == 1)]
prob_fbs_given_male = len(males_high_fbs) / len(males)

print(f"\n2i. P(fasting sugar > 120 | male):")
print(f"Total males: {len(males)}")
print(f"Males with fbs > 120: {len(males_high_fbs)}")
print(f"P(fbs > 120 | male) = {len(males_high_fbs)}/{len(males)} = {prob_fbs_given_male:.4f}")

# 2ii. P(fasting sugar > 120 | female)
females = heart[heart['sex'] == 0]
females_high_fbs = heart[(heart['sex'] == 0) & (heart['fbs'] == 1)]
prob_fbs_given_female = len(females_high_fbs) / len(females)

print(f"\n2ii. P(fasting sugar > 120 | female):")
print(f"Total females: {len(females)}")
print(f"Females with fbs > 120: {len(females_high_fbs)}")
print(f"P(fbs > 120 | female) = {len(females_high_fbs)}/{len(females)} = {prob_fbs_given_female:.4f}")

# 2iii. P(serum 200-239 | male) - need to check cholesterol values
print(f"\nCholesterol distribution:")
print(f"Min: {heart['chol'].min()}, Max: {heart['chol'].max()}")
print(f"Mean: {heart['chol'].mean():.2f}")

males_moderate_chol = heart[(heart['sex'] == 1) & (heart['chol'] >= 200) & (heart['chol'] <= 239)]
prob_moderate_chol_given_male = len(males_moderate_chol) / len(males)

print(f"\n2iii. P(serum 200-239 | male):")
print(f"Males with chol 200-239: {len(males_moderate_chol)}")
print(f"P(chol 200-239 | male) = {len(males_moderate_chol)}/{len(males)} = {prob_moderate_chol_given_male:.4f}")

# 2iv. P(serum 200-239 | female)
females_moderate_chol = heart[(heart['sex'] == 0) & (heart['chol'] >= 200) & (heart['chol'] <= 239)]
prob_moderate_chol_given_female = len(females_moderate_chol) / len(females)

print(f"\n2iv. P(serum 200-239 | female):")
print(f"Females with chol 200-239: {len(females_moderate_chol)}")
print(f"P(chol 200-239 | female) = {len(females_moderate_chol)}/{len(females)} = {prob_moderate_chol_given_female:.4f}")

print("\n" + "="*50)
print("PROBLEM 3: NAIVE BAYES - LOAN APPROVAL")
print("="*50)

print("Dataset shape:", loan.shape)
print("\nDataset:")
print(loan)

print("\nVariable distributions:")
print("\nEmployment Status:")
print(loan['Employment Status'].value_counts())

print("\nCredit History:")
print(loan['Credit History'].value_counts())

print("\nIncome Level:")
print(loan['Income Level'].value_counts())

print("\nCollateral:")
print(loan['Collateral'].value_counts())

print("\nLoan Approved:")
print(loan['Loan Approved'].value_counts())

# Naive Bayes calculation for: Self-employed, Average credit, Low income, No collateral
print("\nNAIVE BAYES CALCULATION:")
print("Predicting for: Self-employed, Average credit history, Low income, No collateral")

total_records = len(loan)
approved_records = len(loan[loan['Loan Approved'] == 'Yes'])
denied_records = len(loan[loan['Loan Approved'] == 'No'])

# Prior probabilities
prob_approved = approved_records / total_records
prob_denied = denied_records / total_records

print(f"\nPrior probabilities:")
print(f"P(Approved) = {approved_records}/{total_records} = {prob_approved:.4f}")
print(f"P(Denied) = {denied_records}/{total_records} = {prob_denied:.4f}")

# Likelihoods for APPROVED class
approved_data = loan[loan['Loan Approved'] == 'Yes']

# P(Self-employed | Approved)
self_employed_approved = len(approved_data[approved_data['Employment Status'] == 'Self-Employed'])
prob_self_emp_given_approved = self_employed_approved / len(approved_data)

# P(Average | Approved)
avg_credit_approved = len(approved_data[approved_data['Credit History'] == 'Average'])
prob_avg_credit_given_approved = avg_credit_approved / len(approved_data)

# P(Low income | Approved)
low_income_approved = len(approved_data[approved_data['Income Level'] == 'Low'])
prob_low_income_given_approved = low_income_approved / len(approved_data)

# P(No collateral | Approved)
no_collateral_approved = len(approved_data[approved_data['Collateral'] == 'No'])
prob_no_collateral_given_approved = no_collateral_approved / len(approved_data)

print(f"\nLikelihoods for APPROVED:")
print(f"P(Self-employed | Approved) = {self_employed_approved}/{len(approved_data)} = {prob_self_emp_given_approved:.4f}")
print(f"P(Average credit | Approved) = {avg_credit_approved}/{len(approved_data)} = {prob_avg_credit_given_approved:.4f}")
print(f"P(Low income | Approved) = {low_income_approved}/{len(approved_data)} = {prob_low_income_given_approved:.4f}")
print(f"P(No collateral | Approved) = {no_collateral_approved}/{len(approved_data)} = {prob_no_collateral_given_approved:.4f}")

# Likelihoods for DENIED class
denied_data = loan[loan['Loan Approved'] == 'No']

# P(Self-employed | Denied)
self_employed_denied = len(denied_data[denied_data['Employment Status'] == 'Self-Employed'])
prob_self_emp_given_denied = self_employed_denied / len(denied_data)

# P(Average | Denied)
avg_credit_denied = len(denied_data[denied_data['Credit History'] == 'Average'])
prob_avg_credit_given_denied = avg_credit_denied / len(denied_data)

# P(Low income | Denied)
low_income_denied = len(denied_data[denied_data['Income Level'] == 'Low'])
prob_low_income_given_denied = low_income_denied / len(denied_data)

# P(No collateral | Denied)
no_collateral_denied = len(denied_data[denied_data['Collateral'] == 'No'])
prob_no_collateral_given_denied = no_collateral_denied / len(denied_data)

print(f"\nLikelihoods for DENIED:")
print(f"P(Self-employed | Denied) = {self_employed_denied}/{len(denied_data)} = {prob_self_emp_given_denied:.4f}")
print(f"P(Average credit | Denied) = {avg_credit_denied}/{len(denied_data)} = {prob_avg_credit_given_denied:.4f}")
print(f"P(Low income | Denied) = {low_income_denied}/{len(denied_data)} = {prob_low_income_given_denied:.4f}")
print(f"P(No collateral | Denied) = {no_collateral_denied}/{len(denied_data)} = {prob_no_collateral_given_denied:.4f}")

# Calculate posterior probabilities
# P(Approved | features) = P(features | Approved) * P(Approved)
prob_features_given_approved = (prob_self_emp_given_approved * 
                               prob_avg_credit_given_approved * 
                               prob_low_income_given_approved * 
                               prob_no_collateral_given_approved)

posterior_approved = prob_features_given_approved * prob_approved

# P(Denied | features) = P(features | Denied) * P(Denied)
prob_features_given_denied = (prob_self_emp_given_denied * 
                             prob_avg_credit_given_denied * 
                             prob_low_income_given_denied * 
                             prob_no_collateral_given_denied)

posterior_denied = prob_features_given_denied * prob_denied

print(f"\nPosterior calculations:")
print(f"P(features | Approved) = {prob_features_given_approved:.6f}")
print(f"P(features | Denied) = {prob_features_given_denied:.6f}")
print(f"P(Approved | features) ∝ {posterior_approved:.8f}")
print(f"P(Denied | features) ∝ {posterior_denied:.8f}")

# Normalize
total_posterior = posterior_approved + posterior_denied
final_prob_approved = posterior_approved / total_posterior
final_prob_denied = posterior_denied / total_posterior

print(f"\nFinal probabilities:")
print(f"P(Approved | features) = {final_prob_approved:.4f}")
print(f"P(Denied | features) = {final_prob_denied:.4f}")

if final_prob_approved > final_prob_denied:
    prediction = "APPROVED"
else:
    prediction = "DENIED"

print(f"\nPREDICTION: The loan would be {prediction}")
print(f"Confidence: {max(final_prob_approved, final_prob_denied):.4f}")