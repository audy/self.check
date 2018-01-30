#!/usr/bin/env python3

from pprint import pprint
import random
import datetime
import json
import os


def parse_response(type, raw_answer):

    if type == 'bool':
        if raw_answer.startswith('y'):
            return True
        elif raw_answer.startswith('n'):
            return False
        else:
            return None
    elif type == 'int':
        return int(raw_answer)
    elif type == 'float':
        return float(raw_answer)
    elif type == 'str':
        return str(raw_answer)
    else:
        print('I don\'t know how to process answer of type {}'.format(type))
        quit(-1)


def query_question(question):

    if question['type'] == 'bool':
        raw_answer = input('{} [y/n]: '.format(question['prompt']))
    elif question['type'] == 'int':
        raw_answer = input('{} [int]: '.format(question['prompt']))
    elif question['type'] == 'float':
        raw_answer = input('{} [float]: '.format(question['prompt']))
    elif question['type'] == 'str':
        raw_answer = input('{} [str]: '.format(question['prompt']))
    else:
        print('can\'t understand question:')
        print(question)
        quit(-1)

    return raw_answer


def get_answer_for_question(question):

    raw_answer = query_question(question)

    parsed_answer = parse_response(question['type'], raw_answer)

    return parsed_answer


def write_responses(responses):

    out_path = os.path.join('responses', str(responses['time']) + '.json')
    with open(out_path, 'w') as handle:
        handle.write(json.dumps(responses))

    print('wrote to {}'.format(out_path))


def main():

    config_path = os.path.expanduser('~/.self-check.json')

    with open(config_path) as handle:
        config = json.loads(handle.read())

    responses = {}

    questions = config['questions']

    responses['time'] = datetime.datetime.now().timestamp()
    print(responses['time'])

    random.shuffle(questions)

    for question in questions:
        answer = get_answer_for_question(question)

        responses[question['id']] = answer

    write_responses(responses)


if __name__ == '__main__':
    main()
