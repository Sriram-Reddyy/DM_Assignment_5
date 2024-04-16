import pytest
from all_questions import *
import pickle



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = 0.0288

    # type: float
    # Calculate the probability.
    answers['(b)'] = 0.002

    # type: float
    # Calculate the probability.
    answers['(c)'] = 0.08
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: False
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] =  False
    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    answers['(c) Weight update'] = "0.5*math.log((1-p)/p)"#0.4236

    # type: float
    # the answer should be correct to 3 significant digits
    answers['(d) Weight influence'] = 1.527
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = "No"

    # type: explain_string
    answers['Explain'] = "Alan’s approach is not effective because flipping a coin is purely random and has no predictive power. It does not take into account any information relevant to stock market movements. Ensemble methods rely on combining predictions from models that are individually better than random chance, which coin flipping is not."
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = "iii"

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = "i"

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = "ii"

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = "iv"
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = "p"

    # type: eval_float
    answers['(a) C2-TPR'] = "2*p"

    # type: eval_float
    answers['(a) C1-FPR'] = "p"

    # type: eval_float
    answers['(a) C2-FPR'] = "2*p"

    # type: string
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = 'no'

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = (
            "C2 doesn't outperform C1 as both exhibit identical expected True Positive Rates (TPR) and False Positive Rates (FPR), positioning them along the random guess line of an ROC curve. This suggests that neither classifier demonstrates predictive capability beyond random chance."
    )

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = 'precision/recall'

    # type: explain_string
    answers['(c) explain'] = (
        "In this context, precision and recall offer more insightful metrics as they account for the trade-off between true positives and the relevance of predictions (precision) and the model's effectiveness in identifying all positive samples (recall). Given that C2 exhibits a higher recall compared to C1, it could be viewed as a superior classifier based on these measures."
    )

    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = 'C2'

    # type: explain_string
    answers['(i) Best classifier, explain'] = (
        "C2 is the better classifier because it has a much higher recall/TPR and F1-measure than C1, indicating it correctly identifies more positive cases and has a better balance between precision and recall."
    )

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = 'precision-recall-F1-Measure'

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = (
        "Precision, recall, and the F1-measure are the suitable metrics as they offer a comprehensive evaluation of a classifier's performance, particularly in scenarios with imbalanced datasets where positive cases are significantly less prevalent than negative ones."
    )

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = 'C2'

    # type: explain_string
    answers['(iii) best classifier, explain'] = (
        "C2 is preferred because it maintains a balance between precision and recall, as indicated by its highest F1-measure among the classifiers. While C3 has the highest precision, it does so at the expense of recall, making it less desirable for cases where identifying all positives is important."
    )

    return answers



#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = "p"

    # type: eval_float
    answers['(a) recall for C0'] = "p"

    # type: eval_float
    answers['(b) F-measure of C0'] = "2 * (0.1 * p) / (0.1 + p)"

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = "yes"

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = 0.3
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] =  {
    'recall': 0.5333,
    'precision': 0.6154,
    'F-measure': 0.5714,
    'accuracy': 0.88
}

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'F-measure'

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'accuracy'

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = (
        "In scenarios characterized by imbalanced classes, such as predicting weather where one outcome is significantly more prevalent, the F-measure emerges as the most suitable metric. It strikes a balance between precision and recall, essential for assessing model performance accurately. Accuracy, on the other hand, might not accurately reflect predictive prowess, particularly for the minority class, as it can be artificially inflated by a large number of true negatives. Therefore, it's considered the least appropriate metric in such imbalanced settings, as it doesn't adequately account for the class distribution and may mask deficiencies in capturing minority class instances."
    )
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = "T1"

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = "T2"

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = "TPR/FPR"

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = (
        "In a medical context where the consequences of missing a diagnosis (false negative) carry significant costs, such as in cancer detection, the True Positive Rate (TPR) and False Positive Rate (FPR) become paramount metrics for evaluating tests T1 and T2. This emphasizes the importance of the test's ability to accurately identify true positives."
    )

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = (
        "In situations where the population being examined has a low prevalence of cancer, false positives can have significant consequences, including psychological distress, exposure to potentially harmful tests, and increased financial burdens from unnecessary diagnostic procedures. In such scenarios, the F-measure becomes a preferred metric over TPR/FPR. The F-measure considers both precision and recall, offering a balanced assessment of a test's performance. This is particularly valuable when the focus is on minimizing false positives while still capturing as many true positives as possible. Prioritizing the F-measure is advisable when follow-up procedures following a positive test result are costly, invasive, or pose risks to the patient. By emphasizing the F-measure, healthcare providers can strive to achieve higher precision, thereby reducing the occurrence of false positives and mitigating the potential adverse effects associated with them."
    )

    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
