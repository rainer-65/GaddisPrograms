# This program displays a sales chart.
import matplotlib.pyplot as plt


def main():
    # Create a list with the X coordinates of each bar's left edge.
    left_edges = [0, 5, 10, 15, 20]

    # Create a list with the heights of each bar.
    heights = [70, 30, 300, 400, 500]

    # Create a variable for the bar width.
    bar_width = 5

    # Build the bar chart.
    plt.bar(left_edges, heights, bar_width, color=('r', 'g', 'b', 'y', 'k'))

    # Add a title.
    plt.title('Sales by Year')

    # Add labels to the axes.
    plt.xlabel('Year')
    plt.ylabel('Sales')

    # Customize the tick marks.
    plt.xticks([0, 5, 10, 15, 30],
               ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 50, 200, 300, 400, 500],
               ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

    # Display the bar chart.
    plt.show()


# Call the main function.
if __name__ == '__main__':
    main()
