import numpy as np
import ANN_functs as ann 
import matplotlib.pyplot as plt

"""
This is the runner script for the articial neural network created by group C07 for the course AE2223-2, Assignment 4. It is used to both train the ANN for various input data and 
to classify the quality of the ANN. Say hello to Bob!
"""

print("Hello, I am Bob! Please tell me what you want to do!")
print("Teach me something new (train an ANN and export weights) [1]")
print("Classify an image [2]")
print("Test my capabilities [3]")

iterationnumber = 1000
learning_rate = 0.3

opt = int(input())

weights_hidden = 0

def training(iterationnumber,learning_rate):
        print("Please enter the training input data file below:")
        #input_filename = str(input())
        input_filename = "PreplanningPlanetype_2_copy.txt"
        learning_input = np.genfromtxt(input_filename,dtype = float)

        print(learning_input)
        
        if input_filename == "PreplanningPlanetype_2_copy.txt":
            learning_input = np.reshape(learning_input,(2686,100))

        print("Please enter the training output data file below:")
        #output_filename = str(input())
        output_filename = "Solutions_planetype.txt"
        learning_output = np.genfromtxt(output_filename, dtype = float, delimiter = " ")
        
        n = np.max(learning_input)
        newlearningoutput = np.zeros((int(max(learning_output)),(len(learning_output))))
        for i in range(len(learning_output)):
            newlearningoutput[int(learning_output[i]-1),i] = 1
        
        learning_output = newlearningoutput

        print("Do you want me to give you updates? [y/n]")
        #wordy = str(input())
        wordy = "y"
        if wordy == "y":
            verbose = True
            print(np.shape(learning_input),np.shape(learning_output))
        
        weights_hidden, bias_hidden, weights_output, bias_output, total_error_series = ann.learn_gradient(learning_input,learning_output,iterationnumber,verbose,learning_rate)

        plt.plot(np.arange(iterationnumber+1),total_error_series)
        plt.yscale("log")
        plt.ylabel("Sum-Squared Error")
        plt.xlabel("Number of Iterations")
        plt.title("Sum-Squared Error of ANN while Learning")
        plt.show()

        return  weights_hidden, bias_hidden, weights_output, bias_output
    

if opt == 1:
    weights_hidden, bias_hidden, weights_output, bias_output = training(iterationnumber,learning_rate)

opt = int(input("What do you want to do now? 1, 2 or 3"))

if opt == 3:
    print("Please enter the testing input data file below:")
    #input_filename = str(input())
    input_filename = "PreplanningPlanetype_2_copy.txt"
    testing_input = np.genfromtxt(input_filename,dtype = float)

    print(testing_input)
    
    if input_filename == "PreplanningPlanetype_2_copy.txt":
        testing_input = np.reshape(testing_input,(2686,100))

    print("Please enter the training output data file below:")
    #output_filename = str(input())
    output_filename = "Solutions_planetype.txt"
    testing_output = np.genfromtxt(output_filename, dtype = float, delimiter = " ")
    
    n = np.max(testing_input)
    newtestingoutput = np.zeros((int(max(testing_output)),(len(testing_output))))
    for i in range(len(testing_output)):
        newtestingoutput[int(testing_output[i]-1),i] = 1
    
    testing_output = newtestingoutput

    print("Do you want me to give you updates? [y/n]")
    #wordy = str(input())
    wordy = "y"
    if wordy == "y":
        verbose = True
        print(np.shape(testing_input),np.shape(testing_output))

    avgaccuracy, seriesaccuracy = ann.test(testing_input,testing_output,weights_hidden,weights_output,bias_hidden,bias_output)
    print(seriesaccuracy)
    print(avgaccuracy)

    plt.plot(seriesaccuracy)
    plt.show()
    
    

    




        

    


