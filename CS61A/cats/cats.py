"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    index = 0
    for paragraph in paragraphs:
        if select(paragraph):
            if index == k:
                return paragraph
            index += 1
    return ''
            
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    #for word in topic:
    #    return lambda z: word in lower(remove_punctuation(z))
    def contain(lst):
        for word in topic:
            if word in split(lower(remove_punctuation(lst))):
                return True
        return False
    return contain
    
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    total = len(typed_words)
    accurate_num = 0

    if len(typed_words) == 0:
        return 0.0
    for i in range(total):
            if i < len(reference_words) and typed_words[i] == reference_words[i]:
                accurate_num += 1
    return (accurate_num/total)*100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return (len(typed)/5)/(elapsed/60)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    
    if user_word in valid_words:
        return user_word

    smallest_difference = min(valid_words, key = lambda word: diff_function(user_word, word, limit))

    if diff_function(user_word, smallest_difference, limit) <= limit:
        return smallest_difference
    else:
        return user_word

    # smallest_diff = limit
    # smallest_word = user_word
    # difference = diff_function(user_word, word, limit)
        # if difference <= smallest_diff: #compare difference to record smallest diff, default record is limit
        #     smallest_diff, smallest_word = difference, word
    #return smallest_word 
    
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    # assert False, 'Remove this line'

    def num_sub(start, goal, limit, num_letters):
        if num_letters > limit:
            return limit + 1

        elif start == "" or goal == "":
            num_letters = num_letters + abs(len(start)-len(goal)) #return letters plus difference in length
            return num_letters
        # if len(start) == 1 or len(goal) == 1:
        #      return num_letters + abs(len(start)-len(goal)) #return letters plus difference in length
       
        else:
            if start[0] != goal[0]:
                num_letters += 1
            return num_sub(start[1:], goal[1:], limit, num_letters)
    return num_sub(start, goal, limit, 0)
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    #assert False, 'Remove this line'


    def patches(start, goal, limit, distance):
        if distance > limit:
            return limit + 1 
        
        # elif start == goal: #return count if remaining words are equal
        #     return distance

        if len(start) > 1 and len(goal) > 1:
            if start[0] == goal[0]: #remove first letter of both words if equal
                return patches(start[1:], goal[1:], limit, distance)
            if start[-1] == goal[-1]: #remove last letter of both words if equal
                return patches(start[:-1], goal[:-1], limit, distance)
            
            elif start[1] == goal[0]: # remove letter: take out first letter of first word
                return patches(start[1:], goal[:], limit, distance + 1)
            elif start[0] == goal[1]: # add letter: take out first letter of second word 
                return patches(start[0:], goal[1:], limit, distance + 1)
            else: # substitute
                return patches(start[1:], goal[1:], limit, distance + 1)
            
        else: #when one of words' length is 1
            if not (start in goal or goal in start):
                distance += 1

        return distance + abs(len(start)-len(goal))

    return patches(start, goal, limit, 0)
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server.
        >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
        >>> typed = ['I', 'have', 'begun']
        >>> prompt = ['I', 'have', 'begun', 'to', 'type']
        >>> print_progress({'id': 1, 'progress': 0.6})
        ID: 1 Progress: 0.6
        0.6
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    correct_count = 0 
    total_count = len(prompt)

    for i in range(len(typed)):
        if typed[i] == prompt[i]:
            correct_count += 1
        else:
            break

    progress = correct_count / total_count
    send({'id': user_id, 'progress': progress })
    return progress #returns ratio

    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    all_times = []

    def find_diff(player_times):
        time_diff = []
        for i in range(len(player_times) - 1):
            time_diff.append(player[i+1] - player[i])
        return time_diff

    for player in times_per_player:
        all_times += [find_diff(player)]


    
    return game(words, all_times)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    words_lst = []
    for p in player_indices:
        words_lst += [[]]

    # p1_words = []
    # p2_words = []
    # for i in word_indices:
    #     if time(game, 0 , i) <= time(game, 1 , i):
    #         p1_words.append(word_at(game, i))
    #     else:
    #         p2_words.append(word_at(game, i))

    for i in word_indices:
        min_player = 0
        for p in player_indices:
            if time(game, p , i) < time(game, min_player , i):
                min_player = p
        words_lst[min_player].append(word_at(game, i))
    return words_lst
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)