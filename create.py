import requests

NOTION_TOKEN = "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"
PARENT_PAGE_ID = "1db7bdaba1c980429bc9de1961b43f55"

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def create_notion_page(title, content_blocks):
    url = "https://api.notion.com/v1/pages"
    data = {
        "parent": {"page_id": PARENT_PAGE_ID},
        "properties": {
            "title": {
                "title": [{"type": "text", "text": {"content": title}}]
            }
        },
        "children": content_blocks
    }
    response = requests.post(url, headers=headers, json=data)
    print("✅ 상태 코드:", response.status_code)
    print(response.json())

title = "📘 Pandas 1강: Series"

content_blocks = [
    {
        "object": "block",
        "type": "heading_2",
        "heading_2": {
            "rich_text": [{"type": "text", "text": {"content": "📌 Pandas Series란?"}}]
        }
    },
    {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [{"type": "text", "text": {
                "content": "Series는 Pandas의 1차원 데이터 구조로, 인덱스를 가진 리스트처럼 생각하면 됩니다."}}]
        }
    },
    {
        "object": "block",
        "type": "heading_3",
        "heading_3": {
            "rich_text": [{"type": "text", "text": {"content": "✅ 기본 생성"}}]
        }
    },
    {
        "object": "block",
        "type": "code",
        "code": {
            "rich_text": [{"type": "text", "text": {"content": "import pandas as pd\ns = pd.Series([10, 20, 30, 40])\nprint(s)"}}],
            "language": "python"
        }
    },
    {
        "object": "block",
        "type": "heading_3",
        "heading_3": {
            "rich_text": [{"type": "text", "text": {"content": "✅ 인덱스 지정"}}]
        }
    },
    {
        "object": "block",
        "type": "code",
        "code": {
            "rich_text": [{"type": "text", "text": {"content": "s2 = pd.Series([100, 200, 300], index=['a', 'b', 'c'])\nprint(s2)"}}],
            "language": "python"
        }
    },
    {
        "object": "block",
        "type": "heading_3",
        "heading_3": {
            "rich_text": [{"type": "text", "text": {"content": "✅ 값 접근과 평균 계산"}}]
        }
    },
    {
        "object": "block",
        "type": "code",
        "code": {
            "rich_text": [{"type": "text", "text": {
                "content": "print(s2['b'])      # 인덱스로 접근\nprint(s2[0])        # 순서로 접근\nprint(s2.mean())    # 평균"}}],
            "language": "python"
        }
    }
]

create_notion_page(title, content_blocks)





