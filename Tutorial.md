1. Đầu tiên là xác định form của mình như thế nào ?
   - Có bao nhiều phần, các phần sẽ được điền nhưu thế nào (điền text hay lựa chọn duy nhất hay lựa chọn nhiều,...)
   - Logic của form : Ví dụ tại 1 câu hỏi nào đó, lựa chọn 1 sẽ rẽ một hướng, lựa chọn 2 sẽ rẽ một hướng khác,... hoặc lựa chọn 1 sẽ cho người dùng tiếp tục điền form, lựa chọn 2 sẽ khiến form kết thúc,....

2. Lấy entryID (ID của câu hỏi) bằng script chạy trên Google Apps Script: 
	- **ClaudeAI** 
		> Sử dụng Google Apps Script để lấy questionID

3. Viết Script: 
	- Sử dụng AI Claude: Prompt : "Sử dụng Google Apps Script để điền số lượng lớn Google Form", tinh chỉnh yêu cầu để Claude sửa code theo đúng dạng form của mình

	- Đưa cho nó list questionID mình đã thu được và yêu cầu nó tự thay vào code cho phù hợp

	- Cơ bản thì cấu trúc script sẽ kiểu như sau
		- Lấy ID Form: Do đã tạo form trước rồi nên ta sẽ điền được ID form ở đây
		- Lấy ID Sheet: Do chưa tạo sheet, ta cứ để trống ID sheet đã rồi chèn vào sau.
		- Trả lời các câu hỏi (entryID):
			- **CHÚ Ý 1**, tùy dạng câu hỏi-câu trả lời mà code sẽ khác 
			- **CHÚ Ý 2**: Định dạng cho sheet phải chuẩn để bên code lấy dữ liệu chuẩn 
				- VD: Trong Sheet: hàng 0 là header, hàng 1 là phiếu trả lời cho câu hỏi đầu tiên, trong hàng 1, cột số 1 là câu trả lời cho câu hỏi số 1, bên code cũng phải lấy đúng dữ liệu từ ô đó để trả lời cho câu hỏi đó. Ta có thể dễ bị nhầm lẫn khi ở bên Sheet định dạng hàng 1 cột 0 trả lời cho câu hỏi số 1 mà bên code ta lại lấy hàng 1 cột 1 để trả lời cho câu hỏi số 1 => lấy không đúng dữ liệu cần lấy => Script khi chạy sẽ báo lỗi.
		- Gửi phiếu trả lời (submit)

4. Viết mã Python tự động gen ra data cho sheet phiếu trả lời
	- Sheet được tạo ra sẽ có cấu trúc: 
		Hàng đầu tiên là Header ghi các câu hỏi, từ các hàng sau, mỗi hàng được coi như 1 phiếu trả lời

		Mỗi cột là câu trả lời cho 1 câu hỏi => mỗi ô sẽ là câu trả lời của một câu hỏi của một phiếu trả lời nào đó
	- Với trường hợp form là dạng chọn các đáp án duy nhất:
		- Thiết lập danh sách các lựa chọn cho câu hỏi
			VD: Câu hỏi 1 (Cột 1) có 4 lựa chọn là "A", "B", "C", "D"

			Ta có thể làm chi tiết hơn ở bước này với các yêu cầu chi tiết về tỉ lệ số lượng các câu trả lời kiểu:
				Với câu hỏi 1, ta cơ cấu để số câu trả lời A là 70%, B là 2%,...

		- Thiết lập số phiếu trả lời muốn có
	- Chạy xong ta sẽ được file CSV

5. Đưa file CSV lên sheet
	- Có thể tạo sheet mới hoặc chèn vào một sheet sẵn có(tùy ý) nhưng nhớ cái sheet chứa data này, ID của nó phải được đưa vào script
		- Đảm bảo như **CHÚ Ý 2**, định dạng của sheet phải chuẩn.
	- Sau khi tạo sheet xong ta sẽ có ID, chèn lại ID này vào script

