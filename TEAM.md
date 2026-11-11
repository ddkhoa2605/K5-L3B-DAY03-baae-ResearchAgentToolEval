# Team

## Thông tin nhóm

- Tên nhóm: baae
- Lớp: L3B
- Repo nhóm: https://github.com/ddkhoa2605/K5-L3B-DAY03-baae-ResearchAgentToolEval
- URL repo, nhánh nộp, commit chốt:  https://github.com/ddkhoa2605/K5-L3B-DAY03-baae-ResearchAgentToolEval · nhánh `main` · commit `<điền khi chốt>`

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
| 1 | Đoàn Đăng Khoa | 2A202603766 | 26ai.khoadd@vinuni.edu.vn | ddkhoa2605 | Prompt & Tool Declaration (v0→v4), điều phối merge |
| 2 | Hồ An Lộc | 2A202603743 | 26ai.locha@vinuni.edu.vn | hoanloc | Eval nhóm, UI, báo cáo |
| 3 | Nguyễn Văn Minh | 2A202603771 | 26ai.minhnv7@vinuni.edu.vn | nguyenvanminh | Tool Engineer & Testing Specialist |

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## DoanDangKhoa-2A202603766

### Phần việc phụ trách

- Chạy baseline v0, phân tích từng case FAIL và gán loại lỗi (CP1).
- Sửa `starter_v0/artifacts/system_prompt.md` và `starter_v0/artifacts/tools.yaml` qua các version v1–v4, mỗi version một giả thuyết (CP2).
- Ghi `starter_v0/artifacts/version_log.csv`; điền B1, B2, mục 3 (Giải pháp), mục 7 (B6. Reflection) trong `report/team/group_report.md`.
- Khai báo 4 tool mới của nhóm trong `tools.yaml` và thêm rule routing tương ứng (v4).

### Đóng góp cụ thể

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


### Bằng chứng

- **Commit** (branch `doandangkhoa`, đã merge vào `main` qua PR #2 và PR #3):
  - `7203903` CP1: baseline v0 run, version log, failure analysis B2
  - `c0f0246` v1: rewrite system prompt (0.65 → 0.95)
  - `2d7c597` v2: rewrite tool descriptions + send/clarify yes_no boundary (0.95 → 0.90)
  - `df5eca5` v3: always clarify yes_no before send, follow-up turns override (0.90 → 0.95)
  - `5db4dca` report: add v3 row to B1
  - `78f376e` v4: declare 4 new team tools + routing rules (0.95 → 0.95)
  - `99d326e` (committer, tác giả là Nguyễn Văn Minh): đưa 4 tool + 12 test vào `main`
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


## HoAnLoc-2A202603743

### Phần việc phụ trách

- Thiết kế & thực thi bộ 10 ca kiểm thử nhóm `starter_v0/data/eval_group.json` (5 single-turn + 5 multi-turn) bao quát các bẫy routing tool mới, tham số thời gian, đổi nguồn và guardrail (C5 — CP4).
- Xây dựng ứng dụng Streamlit trong `starter_v0/app.py`, tích hợp expander hiển thị minh bạch tool calls và tham số JSON; cấu hình tunnel Cloudflare và thực hiện Live chat đa lượt ghi transcript (C6 — CP5).
- Đồng biên soạn Báo cáo Nhóm `report/team/group_report.md` (Phần A, B3, B4, B5) và thiết kế toàn diện Poster HTML `report/team/poster.html` (C7 — CP5).
- Cấu hình và kiểm thử tích hợp gửi tin thật lên kênh Telegram sau luồng xác nhận an toàn 2 bước (Bonus).

### Đóng góp cụ thể

- Thiết kế 10 ca eval nhóm độc lập, chất lượng cao trong `starter_v0/data/eval_group.json` (5 single + 5 multi): bẫy routing 2 tool mới `github_repo` (G01) và `pypi_package` (G06), bẫy `timeframe='month'` (G02), bẫy `search_type='Top'` (G03), bẫy thiếu URL (G04), từ chối ngoài phạm vi (G05), ánh xạ Yann LeCun (G07), đổi timeframe đa lượt (G08), guardrail Telegram (G09), chuyển nguồn triệt để từ Twitter sang web (G10).
- Thực thi chạy group eval với artifact version v4 của nhóm đạt 9/10 PASS (90.0%), điền bảng B3 trung thực theo run log.
- Phát triển ứng dụng Streamlit `starter_v0/app.py`, hiển thị chi tiết các lượt `tool_calls` và `args` qua `st.expander`, không che giấu lỗi.
- Thực hiện phiên Live chat 4 lượt hoàn chỉnh với `chat.py` trên version v4, kiểm chứng hành vi hỏi lại URL và guardrail xin xác nhận trước khi gửi tin (B4).
- Thiết lập kênh Telegram Bot và thực hiện phiên kiểm thử live gửi tin thật sau khi xác nhận có/không, lưu vết transcript minh chứng đầy đủ.
- Thiết kế Poster HTML 1 trang chuẩn Material Design tại `report/team/poster.html` phục vụ trình diễn tại vòng Showdown.

### Bằng chứng

- **Báo cáo cá nhân chi tiết:** `report/team/2A202603743_HoAnLoc.md`.
- **Nhánh làm việc & PR:** Nhánh `2A202603743_HoAnLoc` trên repo nhóm (PR #4 và PR hoàn thiện).
- **Code & Cấu hình:** `starter_v0/data/eval_group.json`, `starter_v0/app.py`, `starter_v0/requirements.txt`, `report/team/poster.html`, `report/team/group_report.md` (Phần A, B3, B4, B5).
- **Runs & Transcripts thật:**
  - Run Group v4: `starter_v0/runs/v4_B_group_openai_20261111T091027249801.json` (9/10 PASS, artifact `v4+p111693171221+tc36c98bfd981`).
  - Transcript Live Chat v4: `starter_v0/transcripts/v4_openai_20261111T091113007111.transcript.json`.
  - Transcript Telegram Bonus v4: `starter_v0/transcripts/v4_openai_20261111T091228314936.transcript.json`.

## NguyenVanMinh-2A202603771

### Phần việc phụ trách

- Nghiên cứu, thiết kế và phát triển 4 công cụ mở rộng (Custom Tools) cho Research Agent: `github_repo`, `pypi_package`, `wiki_summary`, `hn_search` (C4).
- Xây dựng hệ sinh thái 12 Unit Tests độc lập, cô lập 100% offline sử dụng fixture `fake_http` trong `starter_v0/tests/test_tools_todo.py` (C4).
- Kiểm soát và bảo đảm tính tuân thủ hợp đồng hệ thống, giữ cho suite kiểm tra hợp đồng `starter_v0/tests/test_tool_contract.py` luôn đạt 100% xanh (55/55 tests).
- Tham gia chạy thử nghiệm Baseline v0 với OpenRouter, phân tích các failure trace ban đầu.

### Đóng góp cụ thể

- Hiện thực hóa 4 tools kèm tài liệu `TOOL.md` đặc tả schema, đăng ký tập trung vào `starter_v0/tools/__init__.py`.
- Áp dụng nguyên tắc lập trình phòng thủ: không bao giờ raise uncaught exception, validate tham số trước khi request, bóc tách URL và chuẩn hóa input lỏng từ LLM.
- Viết 12 test cases bao phủ happy path, input rỗng/sai định dạng và mã lỗi HTTP 404 (đạt 12/12 PASSED, 0 failed).
- Phối hợp đồng bộ hóa schema 4 công cụ mới vào `tools.yaml` để nhóm đánh giá mở rộng.

### Bằng chứng

- Báo cáo cá nhân chi tiết: `report/team/2A202603771_NguyenVanMinh.md`.
- Code & Unit tests:
  - `starter_v0/tools/github_repo/` (`tool.py`, `TOOL.md`)
  - `starter_v0/tools/pypi_package/` (`tool.py`, `TOOL.md`)
  - `starter_v0/tools/wiki_summary/` (`tool.py`, `TOOL.md`)
  - `starter_v0/tools/hn_search/` (`tool.py`, `TOOL.md`)
  - `starter_v0/tools/__init__.py`
  - `starter_v0/tests/test_tools_todo.py`
- Kết quả kiểm thử: `pytest tests/test_tools_todo.py`: 12 passed; `pytest tests/test_tool_contract.py`: 55 passed.
