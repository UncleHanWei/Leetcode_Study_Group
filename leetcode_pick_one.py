import requests

def get_q_data(url, question) :
    payload = """
    {{
        question(titleSlug: "{title}") {{
            questionFrontendId
            isPaidOnly
            title
            difficulty
            titleSlug
        }}
    }}
    """.format(title=question['titleSlug'])
    headers = {
        'Content-Type': 'application/graphql',
        'Cookie': 'csrftoken=3AmrtZA4q7FKAXkBea1CeMXGUWBO1nIwm8Bv550dBRctPKpbHla0BsCHnkGmM60b'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()['data']['question']


def pickOne(url) :
    payload = """
    {
        randomQuestion(categorySlug:\"algorithms\", filters:{}) {
            titleSlug
            difficulty
        }
    }
    """
    headers = {
        'Content-Type': 'application/graphql',
        'Cookie': 'csrftoken=3AmrtZA4q7FKAXkBea1CeMXGUWBO1nIwm8Bv550dBRctPKpbHla0BsCHnkGmM60b'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    question = response.json()['data']['randomQuestion']
    return question


def main() :
    url = "https://leetcode.com/graphql"
    question = pickOne(url)
    q_data = get_q_data(url, question)
    while q_data['isPaidOnly'] :
        question = pickOne(url)
        q_data = get_q_data(url, question)
    q_data = {
        'questionId': q_data['questionFrontendId'],
        'title': q_data['title'],
        'difficulty': q_data['difficulty'],
        'link': f"https://leetcode.com/problems/{q_data['titleSlug']}"

    }
    return q_data

if __name__ == "__main__" :
    main()