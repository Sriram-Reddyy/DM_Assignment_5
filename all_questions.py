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
    answers['(b) D'] = False

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
    answers['Explain'] = "Because Alan's coin flip ensemble method relies on random events, it misses important patterns or data from the intricate and varied stock market, making it inherently faulty for predicting stock market movements."
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
    answers['(a)'] = 'iii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = 'i'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = 'ii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = 'iv'
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
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = 'no'

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = 'Even though C2 has higher values of both metrics, it is not always a stronger classifier than C1; both classifiers show random performance with equal trade-offs between TPR and FPR.'

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = 'precision/recall'

    # type: explain_string
    answers['(c) explain'] = "In this case, precision and recall provide additional information since they take into account the model's capacity to identify all positive samples (recall) and strike a balance between genuine positives and the prediction's relevance (precision). Based on these measures, C2 might be regarded as a superior classifier than C1, as it has a higher recall."
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = 'C2'

    # type: explain_string
    answers['(i) Best classifier, explain'] = 'Both C1 and C2 have a 50% precision rate, however C2 performs better in recall than C1, identifying 50 percent of real positives as opposed to 10 percent for C1. This means that even with the same precision rate, C2 is more effective at finding positive cases.'

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = 'precision-recall-F1-Measure'

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = "Overall, C2 performs better than C1, as seen by a greater true positive rate and F1-measure (which takes precision and recall into account). C2 is generally a more successful classifier than C1, while having a greater false positive rate, which could be a disadvantage in situations where false positives are expensive. This is indicated by its much increased recall and F1-measure."

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = 'C2'

    # type: explain_string
    answers['(iii) best classifier, explain'] = 'The expenses related to false positives and negatives as well as the particular application requirements determine which of the three classifiers—C1, C2, and C3—to use. When accuracy in positive predictions is crucial and false positives are costly, C3, which has the highest precision and the lowest false positive rate, is the best option. When catching as many positive examples as possible is crucial, C2, which has the highest recall, is the chosen option. C2 is still the best overall choice when taking into account both kinds of errors, while C3 would be preferable for people who value accuracy and reducing false positives.'
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = "0.1*p"

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
    answers['(ii) Explain your choices of best and worst metrics'] = 'When there is a class imbalance, recall and precision are not enough to assess overall performance, as shown by the misleadingly high accuracy of a classifier that predicts frequent events such as rain in an area that is prone to rain. The F-measure is the best performance indicator in these situations since it combines recall and precision into one measure, which helps to overcome the problems caused by class imbalance.'
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = 'T1'

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = 'T2'

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = 'TPR/FPR'

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = "When the significant cost of missing a diagnosis (false negative) surpasses the risks of false positives in medical context and as per the data, TPR/FPR is the ideal measure for evaluating cancer detection tests T1 and T2, emphasizing the importance of the test's ability to correctly identify genuine positives."

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = "In the event that the population being tested has a high probability of not having cancer (a very low prevalence), you might prefer the F-measure over TPR/FPR. False positives can have serious consequences, such as psychological distress, exposure to harmful tests, or financial costs from additional needless diagnostic procedures. In this case, the F-measure would be preferred since it is a measure that considers both true positives and false positives. Furthermore, to guarantee that the test's precision is as high as feasible to lower the amount of false positives, you can give the F-measure priority if the follow-up procedures following a positive test are costly, invasive, or dangerous."
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
