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

iterationnumber = 5

opt = int(input())

if opt == 1:
    print("Please enter the training input data file below:")
    input_filename = str(input())
    learning_input = np.genfromtxt(input_filename,dtype = float,delimiter = ",")

    print("Please enter the training output data file below:")
    output_filename = str(input())
    learning_output = np.genfromtxt(output_filename, dtype = float, delimiter = ",")

    print("Do you want me to give you updates? [y/n]")
    wordy = str(input())
    if wordy == "y":
        verbose = True
    
    weights_hidden, bias_hidden, weights_output, bias_output, total_error_series = ann.learn_gradient(learning_input,learning_output,iterationnumber,verbose)
    
    plt.plot(total_error_series,iterationnumber)
    plt.show()

    print("Please name my new skill:")
    export_file_name = str(input())

    hidden_weights_export = open(export_file_name+"_hidden_weights.txt", "w")
    hidden_weights_export.truncate(0)

    for row in weights_hidden:
        np.savetxt(weights_hidden, row)

    hidden_weights_export.close()



