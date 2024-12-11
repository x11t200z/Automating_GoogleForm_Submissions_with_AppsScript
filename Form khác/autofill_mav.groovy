// Script tự động điền và gửi Google Form
function fillForms() {
  var form = FormApp.openById('1RHBxJhnHdJj7N8j-7P3phA-4JA90H8zhJWUnQ-s1yqs');  // ID của Google Form
  var sheet = SpreadsheetApp.openById('1oA5BeQ4Z7IJNkpMi-Ot2iqxWBZrt28YDcwdWX2kOVUQ').getActiveSheet();
  var data = sheet.getDataRange().getValues();  // Lấy dữ liệu từ Google Sheet

  for (var i = 1; i < data.length; i++) {  // Lặp qua từng dòng dữ liệu
    var formResponse = form.createResponse();

    // PHẦN 1: Thông tin nhân khẩu học
    formResponse.withItemResponse(
      form.getItemById('1884636331').asMultipleChoiceItem().createResponse(data[i][0])  // Giới tính của bạn
    );
    formResponse.withItemResponse(
      form.getItemById('1913894983').asMultipleChoiceItem().createResponse(data[i][1])  // Độ tuổi của bạn
    );
    formResponse.withItemResponse(
      form.getItemById('1984355276').asMultipleChoiceItem().createResponse(data[i][2])  // Bạn đã làm việc tại công ty bao nhiêu năm
    );
    formResponse.withItemResponse(
      form.getItemById('1087918939').asMultipleChoiceItem().createResponse(data[i][3])  // Bộ phận làm việc của bạn
    );

    // PHẦN 2: Nhận thức về ứng dụng AI trong công việc
    formResponse.withItemResponse(
      form.getItemById('1754361314').asMultipleChoiceItem().createResponse(data[i][4])  // Bạn tương tác với những loại ứng dụng AI nào
    );
    formResponse.withItemResponse(
      form.getItemById('2119444981').asGridItem().createResponse([
        parseInt(data[i][5])  // Hiệu quả công cụ AI - Cột 1
      ])
    );
    formResponse.withItemResponse(
      form.getItemById('969455228').asMultipleChoiceItem().createResponse(data[i][6])  // Cách AI giúp đạt mục tiêu
    );

    // PHẦN 3: Điểm mạnh và điểm yếu của AI trong công việc
    formResponse.withItemResponse(
      form.getItemById('1583430322').asCheckboxItem().createResponse([
        data[i][7],  // Ưu điểm - Lựa chọn 1
        data[i][8]   // Ưu điểm - Lựa chọn 2
      ])
    );
    formResponse.withItemResponse(
      form.getItemById('117032328').asCheckboxItem().createResponse([
        data[i][9],  // Hạn chế - Lựa chọn 1
        data[i][10], // Hạn chế - Lựa chọn 2
        data[i][11], // Hạn chế - Lựa chọn 3
        data[i][12]  // Hạn chế - Lựa chọn 4
      ])
    );

    // PHẦN 4: Đề xuất để cải thiện hiệu quả AI
    formResponse.withItemResponse(
      form.getItemById('806521708').asMultipleChoiceItem().createResponse(data[i][13])  // Hỗ trợ từ nhóm hoặc lãnh đạo
    );
    formResponse.withItemResponse(
      form.getItemById('1120095927').asMultipleChoiceItem().createResponse(data[i][14])  // Cải thiện hiệu quả AI
    );

    // Submit form response
    formResponse.submit();
  }
}
