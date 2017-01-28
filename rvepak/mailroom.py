import os
import sys
import prettytable

donors = [('Jack', 1), ('John', 2), ('Ray', 3), ('Kelly', 2), ('Rick', 1)]

maxTriesCount = 0


def inputPrompts():
    '''
    this method prompts for the 3 values
    '''
    global maxTriesCount
    allowedResponsesList = allowedResponses(allowedResponsesMap)
    response = input('Choose an action from the following {}: '.format(
        allowedResponsesList))
    if str(response) not in allowedResponsesList:
        while maxTriesCount < 3:
            print(
                'Response {} is not allowed. Allowed responses are {}. Number of trials left = {}. Please try again.'.
                format(
                    str(response), allowedResponsesList, str(3 -
                                                             maxTriesCount)))
            maxTriesCount += 1
            inputPrompts()
    else:
        returnRoutineToBeCalled(allowedResponsesMap, response)()


def returnRoutineToBeCalled(allowedResponsesMap, response):
    '''
    this method returns the function to be called based on the input response
    '''
    for tpl in allowedResponsesMap:
        if response in tpl[0]:
            return tpl[1]


def allowedResponses(allowedResponsesMap):
    '''
    this method returns allowed responses as a list
    '''
    return [x[0] for x in allowedResponsesMap]


def getDonors():
    '''
    this method lists the available donors
    '''
    return list(set([x[0] for x in donors]))


def sendThankYou():
    '''
    this method is called when send thank you is selected
    '''
    response = input('Enter full name: ')
    response = response.strip(' ')
    if response == 'list':
        print('List of donors is {}'.format(getDonors()))
        sendThankYou()
    else:
        if response not in getDonors():
            print('Adding {} to donors List as the name is not available'.
                  format(response))
            enterDonotAmount(response)
            print('Available Donors are {}'.format(getDonors()))
            inputPrompts()
        else:
            enterDonotAmount(response)
            inputPrompts()


def enterDonotAmount(response):
    '''
    this method appens amounts to the donors DS
    '''
    amount = input('Enter donation amount: ')
    try:
        amount = float(amount)
    except ValueError:
        print('Enter a correct amount please ')
    donors.append((response, amount))
    print('{} - Thank you for the generous donation '.format(response))


def createAReport():
    '''
    this method is called when create a report is selected
    '''
    print('Create a Report')
    summaryList = []
    header = 'Donor Name | Total Given | Number of Gifts | Average Gift'
    for dnr in getDonors():
        donatedAmount = 0
        numberOfGifts = 0
        for dnrName, amt in donors:
            if dnr == dnrName:
                donatedAmount += amt
                numberOfGifts += 1
        summaryList.append([
            dnr, '$ ' + str(donatedAmount), numberOfGifts,
            '$ ' + str(donatedAmount / numberOfGifts)
        ])
    print(prettyReport(header.split('|'), summaryList))
    inputPrompts()


def quit():
    '''
    this method is called when quit is selected
    '''
    print('Exiting..')
    sys.exit()


def prettyReport(header, nestedList):
    tbl = prettytable.PrettyTable(header)
    tbl.padding_width = 1
    for lst in nestedList:
        tbl.add_row(lst)
    return tbl


allowedResponsesMap = [('Send a Thank You', sendThankYou),
                       ('Create a Report', createAReport), ('quit', quit)]


def main():
    '''
    main method
    '''
    #allowedResponsesMap = [('Send a Thank You', sendThankYou),
    #                       ('Create a Report', createAReport), ('quit', quit)]
    inputPrompts()


if __name__ == '__main__':
    main()
