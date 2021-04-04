import numpy as np  
        
def initialize(input_size: int, output_size: int):
    
    hidden_size = np.floor(output_size ** 2)
    weights_hidden = np.random.uniform(-2.4 / input_size, +2.4 / input_size, (int(hidden_size),int(input_size)))
    weights_output = np.random.uniform(low=-2.4 / hidden_size, high=+2.4 / hidden_size, size=(int(output_size),int(hidden_size)))
    bias_hidden = np.random.uniform(low=-2.4 / input_size, high=+2.4 / input_size, size=(1,int(hidden_size)))
    bias_output = np.random.uniform(low=-2.4 / hidden_size, high=+2.4 / hidden_size, size=(1,int(output_size)))

    return weights_hidden, weights_output, bias_hidden, bias_output

def activation_function(X: np.ndarray,type: str):
    if type == "sigmoid":
        y = 1 / (1 + np.exp(-X))
    
    if type == "quadratic":
        raise NotImplementedError

    if type == "cubic":
        raise NotImplementedError
    #TODO implement quadratic and cubic activation functions
    
    return y

def activation_function_derivative(X: np.ndarray, type: str):
  
    if type == "sigmoid":
        y = X*(1-X)

    if type == "quadratic":
        raise NotImplementedError

    if type == "cubic":
        raise NotImplementedError

    #TODO implement quadratic and cubic activation functions
    
    return y        


def fprop(input_layer_values: np.ndarray, weights_hidden: np.ndarray, weights_output: np.ndarray, bias_hidden: np.ndarray, bias_output: np.ndarray):
    hidden_layer_values = np.array(activation_function(np.dot(weights_hidden, input_layer_values.T)-bias_hidden,"sigmoid"))
    output_layer_values = np.array(activation_function(np.dot(weights_output, hidden_layer_values.T[:,0])-bias_output,"sigmoid"))
    return hidden_layer_values, output_layer_values

def bprop(input_layer_values: np.ndarray, hidden_layer_values: np.ndarray, output_layer_values: np.ndarray, desired_output: np.ndarray, weights_hidden: np.ndarray, 
                                                        weights_output: np.ndarray, bias_hidden: np.ndarray, bias_output: np.ndarray, learning_rate: float):
    """
    Backwards propagation using the error gradient of the neural network as described by Negnevitsky. Here the weights and biases for each neuron and neural connection are adjusted proportionally
    to the gradient of the respective weight or bias w.r.t the total error
    """
    output_error = desired_output - output_layer_values #error of the neural network
    output_error_gradient = output_error * activation_function_derivative(output_layer_values,"sigmoid") #error gradient in output layer
    weights_output_change = (learning_rate * np.outer(hidden_layer_values,output_error_gradient)).T #change in weights to the output layer
    bias_output_change = learning_rate * -output_error_gradient #change in bias of neurons in output layer
    hidden_error_gradient = np.sum((weights_output * output_error_gradient.T),axis = 0) * activation_function_derivative(hidden_layer_values,"sigmoid") #error gradient in hidden layer
    weights_hidden_change = (np.outer(input_layer_values, hidden_error_gradient)*learning_rate).T #change in weights to the hidden layer
    bias_hidden_change = learning_rate * -hidden_error_gradient #change in bias to the neurons in hidden layer

    weights_hidden += weights_hidden_change
    bias_hidden += bias_hidden_change
    weights_output += weights_output_change
    bias_output += bias_output_change

    total_error = np.sum(output_error**2)/2 #calculating the total error, so that output_error = sum of d(total_error)/d(error for one output neuron)
    return weights_hidden, bias_hidden, weights_output, bias_output, total_error


def learn_gradient(learning_input: np.ndarray, learning_output: np.ndarray, iteration_number: int, verbose: bool, learning_rate: float):
    """
    Implement error gradient learning as discussed in Negnevitsky. It uses forward and backwards propagation, a set of training data, a set of actual classification results, and desired numbers of 
    iteration numbers (epochs.)
    """    
    total_error_series = []
    p = 0
    order = np.arange(0, len(learning_input[0,:]),dtype = int)

    if verbose:
        print("Beginning learning process...")
        print("Input Layer size:", np.shape(learning_input[:,0]), "Output Layer Size", np.shape(learning_output[:,0]))

    weights_hidden, weights_output, bias_hidden, bias_output = initialize(int(len(learning_input[:,0])),int(len(learning_output[:,0])))

    if verbose:
        print(np.shape(weights_hidden), np.shape(weights_output), np.shape(bias_hidden), np.shape(bias_output))
        
    while p <= iteration_number:
        if verbose:
            print("Current iteration number: ", p)
    
        total_error_current = 0.
        np.random.shuffle(order)


        for j in range(len(learning_input[0,:])): 
            current_learning_input = learning_input[:,order[j]]
            current_learning_output = learning_output[:,order[j]]
            #Calculating the activations of all neurons
            hidden_layer_values, output_layer_values = fprop(current_learning_input,weights_hidden,weights_output,bias_hidden,bias_output)

            #Adjusting the weights based on each learning input using backwards propagation
            weights_hidden, bias_hidden, weights_output, bias_output, total_error = bprop(current_learning_input,hidden_layer_values,output_layer_values,
                                                                            current_learning_output,weights_hidden,weights_output, bias_hidden,bias_output,learning_rate)
            total_error_current += total_error
        
        total_error_series = np.append(total_error_series,total_error_current/len(learning_input[0,:]))
        p += 1


    return weights_hidden, bias_hidden, weights_output, bias_output, total_error_series

def test(testing_input: np.ndarray, testing_output: np.ndarray, weights_hidden: np.ndarray, weights_output: np.ndarray, bias_hidden: np.ndarray, bias_output: np.ndarray):
    serialaccuracy = []
    for j in range(len(testing_input[0,:])): 
        #Calculating the output of the ANN
        current_testing_input = testing_input[:,j]
        current_testing_output = testing_output[:,j]

        _, output_layer_values = fprop(current_testing_input,weights_hidden,weights_output,bias_hidden,bias_output)
        print("Testing image number: ", j)
        print("Output of ANN ",output_layer_values)
        decision = np.zeros(np.shape(output_layer_values))
        decision[0,np.argmax(output_layer_values)] = 1
        print("Decision of ANN: ",decision)
        print("Real Classification: ",current_testing_output)
        true_negative = 0
        true_positive = 0
        false_positive = 0
        false_negative = 0
        
        for i in range(len(current_testing_output)):
            if decision[0,i] == current_testing_output[i] and decision[0,i] == 0:
                true_negative += 1
            
            if decision[0,i] == current_testing_output[i] and decision[0,i] == 1:
                true_positive += 1
            
            if decision[0,i] != current_testing_output[i] and decision[0,i] == 0:
                false_negative += 1

            if decision[0,i] != current_testing_output[i] and decision[0,i] == 1:
                false_positive += 1
        
        accuracy = (true_positive+true_negative)/(true_negative+true_positive+false_negative+false_positive)
        print(accuracy)

        serialaccuracy = np.append(serialaccuracy,accuracy)

    avgaccuracy = np.average(serialaccuracy)
    return avgaccuracy, serialaccuracy


        





