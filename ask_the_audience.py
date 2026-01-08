import matplotlib.pyplot as plt 

def main(left,height):
      
    tick_label = ['A', 'B', 'C', 'D'] 
      
    plt.bar(left, height, tick_label = tick_label, 
            width = 0.8, color = ['red', 'green',"blue","yellow"]) 
      
    plt.xlabel('x - axis') 

    plt.ylabel('y - axis') 

    plt.title('Results') 
      
    fig = plt.gcf()

    fig.show()

    print("BUG")
