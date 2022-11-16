import os
import random
import GazeDataLine


def store_gaze_data(text_line):
    tokens = text_line.split()
    return GazeDataLine.Gaze_Data_Line(int(tokens[0]), int(tokens[1]), int(tokens[2]), int(tokens[3]), int(tokens[4]))

#This function assumes that all of the relevant data files are ordered in the same way for each participant.
#Later on, maybe we can fix that?
def visualize_file(directory, file):
    participant_directory = os.path.join(directory, file)
    graph_fixation_file = file + ".graphFXD.txt"
    tree_fixation_file = file + ".treeFXD.txt"
    graph_file = os.path.join(participant_directory, graph_fixation_file)
    tree_file = os.path.join(participant_directory, tree_fixation_file)

    print("We have " + graph_fixation_file + " and " + tree_fixation_file)
    graph_data_lines = []
    tree_data_lines = []
    #Check if valid files:
    if(os.path.isfile(graph_file) and os.path.isfile(tree_file)):
        graph_data = open(graph_file, "r")
        for line in graph_data.readlines():
            new_data = store_gaze_data(line)
            graph_data_lines.append(new_data)
            print(str(graph_data_lines[len(graph_data_lines) - 1]))

        tree_data = open(tree_file, "r")
        for line in tree_data.readlines():
            new_data = store_gaze_data(line)
            tree_data_lines.append(new_data)
            print(str(tree_data_lines[len(tree_data_lines) - 1]))

    graph_data.close()
    tree_data.close()

directory = 'Archive'
print("Randomly selecting a participant to visualize.")
selection = random.randrange(2, 34)

#The macOS file throws off indexing, so we basically need to offset everything by one.
n = 1
for filename in os.listdir(directory):
    n += 1
    if(n == selection + 1):
        print("Visualizing " + filename)
        visualize_file(directory, filename)