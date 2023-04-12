import os
import csv

# create csv path so we can read it
csvpath = os.path.join('Resources', 'budget_data.csv')

# open and read csv
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)

    # create empty lists to store the 2 columns of data seperately 
    months = []
    profit_loss = []
    
    # iterate through the rows of the csv and append the 2 lists 
    for row in csv_reader:
        months.append(row[0])
        profit_loss.append(int(row[1]))
    
    # find all asked information
    total_months = len(months)
    total_pl = sum(profit_loss)

    change_pl = []
    for i in range(1, len(profit_loss)):
        change_pl.append(profit_loss[i] - profit_loss[i-1])
    
    avg_change = round(sum(change_pl)/len(change_pl), 2)

    greatest = max(change_pl)

    least = min(change_pl)

    greatest_month = months[change_pl.index(greatest)+1]

    least_month = months[change_pl.index(least)+1]

    # exibit on method of saving the statements as variable to add to csv
    title = ("Financial Analysis")
    lines = ("-------------------------")
    tm_print=(f"Total Months: {total_months}")
    t_print=(f"Total: ${total_pl}")
    avg_print=(f"Average Change: ${avg_change}")
    inc_print=(f"Greatest Increase in Profits: {greatest_month} (${greatest})")
    dec_print=(f"Greatest Decrease in Profits: {least_month} (${least})")
    
    #print the results
    print(title)
    print(lines)
    print(tm_print)
    print(t_print)
    print(avg_print)
    print(inc_print)
    print(dec_print)

# create path for writing to a csv
output_path = os.path.join("analysis", "analysis.csv")    

# open the new csv 
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile)

    # write the results to the csv
    csvwriter.writerow([title])
    csvwriter.writerow([lines])
    csvwriter.writerow([tm_print])
    csvwriter.writerow([t_print])
    csvwriter.writerow([avg_print])

    csvwriter.writerow([inc_print])

    csvwriter.writerow([dec_print])
   

