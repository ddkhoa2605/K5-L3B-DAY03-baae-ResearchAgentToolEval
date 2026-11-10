# Báo cáo cá nhân — Đoàn Đăng Khoa

## 1. Thông tin thành viên

- Họ tên: Đoàn Đăng Khoa
- MSSV: `2A202603766`
- Email: `26ai.khoadd@vinuni.edu.vn`
- GitHub: `ddkhoa2605`
- Vai trò trong nhóm: **A — Prompt & tool declaration, vòng tối ưu v0→v4** (rubric C1, C2, C3), kiêm điều phối merge vào `main`.

## 2. Phần việc phụ trách

- Chạy baseline v0, phân tích từng case FAIL và gán loại lỗi (CP1).
- Sửa `starter_v0/artifacts/system_prompt.md` và `starter_v0/artifacts/tools.yaml` qua các version v1–v4, mỗi version một giả thuyết (CP2).
- Ghi `starter_v0/artifacts/version_log.csv`; điền B1, B2, mục 3 (Giải pháp), mục 7 (B6. Reflection) trong `report/team/group_report.md`.
- Khai báo 4 tool mới của nhóm trong `tools.yaml` và thêm rule routing tương ứng (v4).

## 3. Đóng góp cụ thể

**Vòng tối ưu** (model `gpt-4o-mini`; v0 qua OpenRouter, v1–v4 qua provider `openai`, cùng model):

| Version | File sửa | Giả thuyết | case_accuracy | Kết quả |
|---|---|---|---:|---|
| v0 | — | Baseline starter | 0.65 | 7 FAIL; 5/7 do chỉ dẫn xấu trong prompt, 2/7 do args `lookup` |
| v1 | `system_prompt.md` | Bỏ chỉ dẫn xấu, thêm rule clarify / xác nhận / từ chối ngoài phạm vi | 0.65 → 0.95 | Sửa 6/7 case. R03, R13 cũng PASS dù dự đoán cần sửa yaml |
| v2 | `tools.yaml` | Viết rõ boundary `yes_no` của `send`/`clarify` thì R12 PASS | 0.95 → 0.90 | **Giả thuyết sai**: R12 vẫn FAIL, M06 bị regression |
| v3 | `system_prompt.md` | Câu "show the exact text" gây R12; thiếu rule lượt sau ghi đè gây M06 | 0.90 → 0.95 | M06 sửa được; R12 vẫn FAIL |
| v4 | `tools.yaml` + `system_prompt.md` | Thêm 4 tool mới không làm base tụt | 0.95 → 0.95 | Không regression, không case base nào gọi nhầm tool mới |

**Phân tích lỗi:**
- Viết bảng B2 cho 7 case FAIL của v0 từ `actual_tool_calls`, `failures`, `observed_mismatch` trong run JSON.
- Ghi chú chỗ nhãn `failure_type` của case (ví dụ R03 là `wrong_tool`) khác với lỗi thực tế quan sát được (`wrong_arg_value`).
- Sau v1, cập nhật B2 bằng kết quả thực tế để so với dự đoán ban đầu.

**Phối hợp nhóm:**
- Cùng nhau bàn luận, lựa chọn 1 tool phù hợp để cả nhóm cùng hướng đến.
- Lên plan, phân chia role cụ thể trong bài lab để có thể có kết quả tốt.
- Review lại các phần mà thành viên khác của nhóm đã làm và ghi trong main để hoàn chỉnh.



## 4. Bằng chứng

- **Commit** (branch `doandangkhoa`, đã merge vào `main` qua PR #2, #3, #6, #7):
  - `7203903` CP1: baseline v0 run, version log, failure analysis B2
  - `c0f0246` v1: rewrite system prompt (0.65 → 0.95)
  - `2d7c597` v2: rewrite tool descriptions + send/clarify yes_no boundary (0.95 → 0.90)
  - `df5eca5` v3: always clarify yes_no before send, follow-up turns override (0.90 → 0.95)
  - `5db4dca` report: add v3 row to B1
  - `78f376e` v4: declare 4 new team tools + routing rules (0.95 → 0.95)
  - `99d326e` (committer, tác giả là Nguyễn Văn Minh): đưa 4 tool + 12 test vào `main`
  - `ca83a7e` khôi phục `system_prompt.md`, `tools.yaml`, `version_log.csv` về v4 và B1/B2; thêm mục 3, 7 của group report và báo cáo cá nhân
  - `090ebfb` điền `TEAM.md` (thông tin repo, vai trò, mục cá nhân) và sửa định dạng bảng/heading
- **Run JSON** (`starter_v0/runs/`), tất cả có `provider_error_cases = 0`, `measured_cases = 20`:
  - `v0_B_base_openrouter_20261110T174226406183.json`
  - `v1_B_base_openai_20261110T182945282365.json`
  - `v2_B_base_openai_20261110T190148454639.json`
  - `v3_B_base_openai_20261110T191415319980.json`
  - `v4_B_base_openai_20261110T194355555650.json`
- **Artifact:** `starter_v0/artifacts/system_prompt.md`, `starter_v0/artifacts/tools.yaml`, `starter_v0/artifacts/version_log.csv`.
- **Report:** `report/team/group_report.md`, các mục 1, 3, B1, B2, 7.
- **AI/công cụ đã dùng và cách tự kiểm tra kết quả:**
  - Dùng **Claude Code (Claude)** để:
    - đọc và tóm tắt run JSON, liệt kê case FAIL kèm `actual_tool_calls`;
    - Nháp nội dung `system_prompt.md`, `tools.yaml` và các phần báo cáo;
    - debate về system prompt xem còn thiếu xót gì không
  - Cách tự kiểm tra:
    - Đọc và tự chỉnh từng rule prompt / description trước khi chạy.
    - Mọi metric đều lấy từ run thật do mình chạy `run_eval.py`; với mỗi run kiểm tra `provider_error_cases = 0` và `measured_cases = total_cases`.
    - Đối chiếu `prompt_hash`/`tools_hash` trong run với hash của file hiện tại để chắc run đúng version.
    - Chạy `pytest` (contract test) sau mỗi lần sửa yaml.
    - So sánh từng case giữa hai version để phát hiện regression thay vì chỉ nhìn tổng điểm.
  - Ví dụ AI/mình làm sai và đã sửa:
    - Lần chạy v1 đầu tiên, prompt mới được dán thêm vào bên dưới prompt starter thay vì thay thế, nên các chỉ dẫn xấu cũ vẫn còn. Kết quả lần đó chỉ đạt 0.80, R10 vẫn tự đoán `timeline(screenname="sama")`. Phát hiện bằng cách đọc `actual_tool_calls` của case FAIL trong run JSON và mở lại `system_prompt.md`. Đã xoá phần prompt cũ và chạy lại v1 (0.95, run `v1_B_base_openai_20261110T182945282365.json`); run lỗi không được ghi vào `version_log.csv`. Cùng lúc đó một dòng routing `social_search` bị cắt cụt khi dán và không được phát hiện ngay; dòng này được sửa ở v3. Bài học: luôn kiểm tra nội dung file và hash trước khi chạy eval.

## 5. Tự đánh giá

- **Làm tốt:**
  - Phân công, lên kế hoạch để làm việc nhóm tối ưu
  - Giữ đúng vòng giả thuyết → sửa → đo, mỗi version một file thay đổi chính.
  - Ghi trung thực version không tăng điểm (v2) và giả thuyết sai.
  - Phân tích được fix nào thuộc prompt, fix nào thuộc yaml dựa trên bằng chứng.
- **Chưa tốt:**
  - R12 chưa giải quyết được sau 3 version.
  - Mỗi version chỉ chạy 1 lần nên chưa đo được độ nhiễu.
- **Bài học:**
  - Model ưu tiên system prompt hơn tool description khi hai bên mâu thuẫn.
  - Rule hành vi đặt trong prompt hiệu quả hơn trên bộ eval này.
  - Cần đọc từng case chứ không chỉ nhìn `case_accuracy`.
- **Tự chấm phần mình phụ trách (C1–C3):** 45/45 (C1: 10/10 · C2: 15/15 · C3: 20/20)
