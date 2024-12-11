import random
import pandas as pd

# Các câu hỏi và đáp án trong form khảo sát
questions = [
    {
        "question": "Giới tính của bạn?",
        "choices": ["Nam", "Nữ"],
        "weights": [0.6, 0.4]  # Nam 60%, Nữ 40%
    },
    {
        "question": "Độ tuổi của bạn?",
        "choices": ["18-34", "35-44", "45 tuổi trở lên"],
        "weights": [0.435, 0.4, 0.165]  # 18-34 tuổi 43.5%, 35-44 tuổi 40%, 45 tuổi trở lên 16.5%
    },
    {
        "question": "Bạn đã làm việc tại công ty bao nhiêu năm?",
        "choices": ["1-3 năm", "3-6 năm", "6-9 năm", "Hơn 9 năm"],
        "weights": [0.33, 0.265, 0.2, 0.205]  # 1-3 năm 33%, 3-6 năm 26.5%, 6-9 năm 20%, Hơn 9 năm 20.5%
    },
    {
        "question": "Bộ phận làm việc của bạn?",
        "choices": ["Nhân sự", "Tài chính", "Công nghệ thông tin", "Marketing", "Khác"],
        "weights": [0.17, 0.295, 0.27, 0.1, 0.165]  # Nhân sự 17%, Tài chính 29.5%, Công nghệ thông tin 27%, Marketing 10%, Khác 16.5%
    },
    {
        "question": "Bạn tương tác với những loại ứng dụng AI nào trong công việc hàng ngày của mình?",
        "choices": ["Học máy để phân tích dữ liệu", "Trò chuyện với chatbot và hỗ trợ khách hàng", "Tự động hóa quy trình (RPA)", "Phân tích dự đoán", "Nhận dạng hình ảnh hoặc giọng nói", "Khác"],
        "weights": [0.24, 0.175, 0.22, 0.135, 0.1, 0.13]  # Các loại ứng dụng AI với tỷ lệ cho mỗi đáp án
    },
    {
        "question": "Hãy đánh giá hiệu quả của các công cụ AI như thế nào trong việc giúp bạn hoàn thành nhiệm vụ của mình?",
        "choices": ["1", "2", "3", "4", "5"],
        "weights": [0.05, 0.08, 0.15, 0.5, 0.22]  # Tỷ lệ cho các mức độ đánh giá
    },
    {
        "question": "Các công cụ AI giúp bạn đạt được mục tiêu công việc theo những cách nào?",
        "choices": ["Cải thiện hiệu quả", "Cung cấp thông tin chi tiết dựa trên dữ liệu", "Giảm khối lượng công việc thủ công", "Hiểu sâu hơn về nhu cầu và sở thích của khách hàng", "Nâng cao hiệu quả trong giao tiếp với khách hàng"],
        "weights": [0.3, 0.19, 0.185, 0.115, 0.21]  # Tỷ lệ cho các cách AI hỗ trợ đạt mục tiêu công việc
    },
    {
        "question": "Ưu điểm của các công cụ AI mà bạn sử dụng là gì 1?",
        "choices": ["Tăng hiệu quả công việc", "Tiết kiệm thời gian", "Giảm thiểu lỗi và cải thiện độ chính xác trong công việc", "Hỗ trợ đưa ra các quyết định nhanh chóng hơn"],
        "weights": [0.15, 0.15, 0.10, 0.10]
    },
    {
        "question": "Ưu điểm của các công cụ AI mà bạn sử dụng là gì 2?",
        "choices": ["Tăng hiệu quả công việc", "Tiết kiệm thời gian", "Giảm thiểu lỗi và cải thiện độ chính xác trong công việc", "Hỗ trợ đưa ra các quyết định nhanh chóng hơn"],
        "weights": [0.15, 0.15, 0.10, 0.10]
    },
    {
    "question": "Hạn chế hoặc thách thức của AI trong công việc 1?",
    "choices": [
        "Giao diện khó sử dụng hoặc khó làm quen", 
        "Khó tận dụng hết các tính năng của AI để hỗ trợ công việc hiệu quả", 
        "Khó diễn giải kết quả hoặc hiểu cách AI đưa ra phân tích", 
        "Phụ thuộc vào chất lượng dữ liệu đầu vào, làm ảnh hưởng đến kết quả", 
        "Thiếu sự linh hoạt của AI trong việc áp dụng vào các nhiệm vụ đặc thù", 
        "Khó khăn trong việc học cách sử dụng hoặc làm quen với công cụ AI", 
        "Khả năng tối ưu hóa công việc bằng công cụ AI còn hạn chế", 
        "Mối quan ngại về quyền riêng tư dữ liệu và bảo mật thông tin", 
        "Mối quan tâm về đạo đức hoặc tuân thủ các quy định liên quan đến AI"
    ],
    "weights": [0.05, 0.07, 0.06, 0.06, 0.05, 0.05, 0.05, 0.12, 0.13]
    },
    {
        "question": "Hạn chế hoặc thách thức của AI trong công việc 2?",
        "choices": [
            "Giao diện khó sử dụng hoặc khó làm quen", 
            "Khó tận dụng hết các tính năng của AI để hỗ trợ công việc hiệu quả", 
            "Khó diễn giải kết quả hoặc hiểu cách AI đưa ra phân tích", 
            "Phụ thuộc vào chất lượng dữ liệu đầu vào, làm ảnh hưởng đến kết quả", 
            "Thiếu sự linh hoạt của AI trong việc áp dụng vào các nhiệm vụ đặc thù", 
            "Khó khăn trong việc học cách sử dụng hoặc làm quen với công cụ AI", 
            "Khả năng tối ưu hóa công việc bằng công cụ AI còn hạn chế", 
            "Mối quan ngại về quyền riêng tư dữ liệu và bảo mật thông tin", 
            "Mối quan tâm về đạo đức hoặc tuân thủ các quy định liên quan đến AI"
        ],
        "weights": [0.06, 0.07, 0.06, 0.05, 0.07, 0.05, 0.06, 0.12, 0.12]
    },
    {
        "question": "Hạn chế hoặc thách thức của AI trong công việc 3?",
        "choices": [
            "Giao diện khó sử dụng hoặc khó làm quen", 
            "Khó tận dụng hết các tính năng của AI để hỗ trợ công việc hiệu quả", 
            "Khó diễn giải kết quả hoặc hiểu cách AI đưa ra phân tích", 
            "Phụ thuộc vào chất lượng dữ liệu đầu vào, làm ảnh hưởng đến kết quả", 
            "Thiếu sự linh hoạt của AI trong việc áp dụng vào các nhiệm vụ đặc thù", 
            "Khó khăn trong việc học cách sử dụng hoặc làm quen với công cụ AI", 
            "Khả năng tối ưu hóa công việc bằng công cụ AI còn hạn chế", 
            "Mối quan ngại về quyền riêng tư dữ liệu và bảo mật thông tin", 
            "Mối quan tâm về đạo đức hoặc tuân thủ các quy định liên quan đến AI"
        ],
        "weights": [0.05, 0.06, 0.07, 0.07, 0.05, 0.05, 0.06, 0.13, 0.12]
    },
    {
        "question": "Hạn chế hoặc thách thức của AI trong công việc 4?",
        "choices": [
            "Giao diện khó sử dụng hoặc khó làm quen", 
            "Khó tận dụng hết các tính năng của AI để hỗ trợ công việc hiệu quả", 
            "Khó diễn giải kết quả hoặc hiểu cách AI đưa ra phân tích", 
            "Phụ thuộc vào chất lượng dữ liệu đầu vào, làm ảnh hưởng đến kết quả", 
            "Thiếu sự linh hoạt của AI trong việc áp dụng vào các nhiệm vụ đặc thù", 
            "Khó khăn trong việc học cách sử dụng hoặc làm quen với công cụ AI", 
            "Khả năng tối ưu hóa công việc bằng công cụ AI còn hạn chế", 
            "Mối quan ngại về quyền riêng tư dữ liệu và bảo mật thông tin", 
            "Mối quan tâm về đạo đức hoặc tuân thủ các quy định liên quan đến AI"
        ],
        "weights": [0.06, 0.06, 0.07, 0.07, 0.05, 0.05, 0.05, 0.12, 0.12]
    }
    ,
    {
        "question": "Bạn cảm thấy nhóm hoặc ban lãnh đạo của mình hỗ trợ bạn giải quyết các thách thức liên quan đến AI như thế nào?",
        "choices": ["Không ủng hộ", "Trung lập", "Ủng hộ"],
        "weights": [0.3, 0.3, 0.4]
    },
    {
        "question": "Bạn tin rằng hành động nào sẽ cải thiện hiệu quả nhất của các công cụ AI trong công việc của bạn?",
        "choices": ["Cải thiện chất lượng dữ liệu", "Cung cấp đào tạo bổ sung", "Đầu tư vào các công cụ AI tốt hơn", "Tăng cường giám sát và trách nhiệm giải trình", "Tăng ngân sách bảo trì AI", "Khác"],
        "weights": [0.2, 0.2, 0.2, 0.2, 0.1, 0.1]
    }
]

# Hàm sinh ra một câu trả lời ngẫu nhiên cho mỗi câu hỏi
def generate_response(question):
        return random.choices(question["choices"], weights=question["weights"], k=1)[0]
# Hàm sinh ra một bộ trả lời cho tất cả các câu hỏi
def generate_survey_response():
    responses = {}
    for question in questions:
        response = generate_response(question)
        responses[question["question"]] = response
    return responses

# Sinh ra 5 bộ trả lời khảo sát ngẫu nhiên
survey_responses = [generate_survey_response() for _ in range(200)]

# Chuyển dữ liệu thành bảng pandas DataFrame
df = pd.DataFrame(survey_responses)

# Lưu kết quả ra file CSV
df.to_csv('survey_responses_with_custom_weights.csv', index=False)

print("Kết quả đã được lưu vào file 'survey_responses_with_custom_weights.csv'.")