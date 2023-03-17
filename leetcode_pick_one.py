import requests

def pickOne(url) :
    payload = """
    {
        randomQuestion(categorySlug:\"algorithms\", filters:{}) {
            questionFrontendId
            isPaidOnly
            title
            difficulty
            titleSlug
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
    q_data = pickOne(url)
    while q_data['isPaidOnly'] :
        q_data = pickOne(url)
    q_data = {
        'questionId': q_data['questionFrontendId'],
        'title': q_data['title'],
        'difficulty': q_data['difficulty'],
        'link': f"https://leetcode.com/problems/{q_data['titleSlug']}"

    }
    return q_data

if __name__ == "__main__" :
    main()