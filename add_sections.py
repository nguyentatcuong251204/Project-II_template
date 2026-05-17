import os

fp = r"d:\BS_thesis\DATN\Report\chapter_datn\methodology.tex"

with open(fp, "r", encoding="utf-8") as f:
    content = f.read()

new_content = r"""

% ================================================================
\section{Đặc tả không gian tương tác cho Học tăng cường (Gymnasium Environment)}
% ================================================================

Để thuật toán Học tăng cường (PPO, SAC) có thể tương tác và học hỏi, toàn bộ hệ thống điện và bài toán tối ưu hai tầng được gói gọn lại thành một môi trường chuẩn hóa theo chuẩn \textbf{Gymnasium}. 

\subsection{Không gian quan sát (Observation Space / State)}
Thay vì để tác tử nhìn thấy toàn bộ ma trận dữ liệu khổng lồ của lưới điện, hệ thống trích xuất một véctơ trạng thái $\mathbf{s}$ chứa các đặc trưng cốt lõi mang tính tóm tắt và được chuẩn hóa về dải $[-1, 1]$:
\begin{itemize}
    \item \textbf{Đặc trưng cấp vùng (Zonal Features):} Đối với mỗi vùng $z$, véctơ trạng thái chứa 4 giá trị:
    \begin{enumerate}
        \item Công suất hiện hữu: $C_{z}^{\text{exist}} / C_{\text{max\_sys}}$
        \item Phụ tải đỉnh: $D_{z}^{\text{peak}} / D_{\text{max\_sys}}$
        \item Phụ tải trung bình: $\bar{D}_{z} / D_{\text{max\_sys}}$
        \item Biên dự phòng (Reserve Margin): $(C_{z}^{\text{exist}} - D_{z}^{\text{peak}}) / \max(1, D_{z}^{\text{peak}})$
    \end{enumerate}
    \item \textbf{Đặc trưng cấp hệ thống (Global Features):} Gồm 3 giá trị: Tổng công suất hệ thống, Tổng phụ tải đỉnh hệ thống, và Hệ số phụ tải (Load Factor).
\end{itemize}
Với hệ thống 3 vùng, véctơ trạng thái sẽ có độ dài là $3 \times 4 + 3 = 15$ chiều. Sự cô đọng này giúp mạng nơ-ron hội tụ nhanh hơn và giảm thiểu hiện tượng quá khớp (overfitting).

\subsection{Không gian hành động (Action Space) và Phần thưởng (Reward)}
\begin{itemize}
    \item \textbf{Hành động $\mathbf{a}$:} Là véctơ công suất đầu tư liên tục, ví dụ với 3 vùng và 4 công nghệ, $\mathbf{a} \in \mathbb{R}^{12}$. Tác tử sẽ đưa ra các giá trị trong giới hạn công suất cho phép (ví dụ: tối đa 2000 MW cho Điện mặt trời mỗi vùng).
    \item \textbf{Cơ chế phần thưởng (Reward Shaping):} Hàm phần thưởng được thiết kế trực tiếp từ hàm phạt tổng quát của bài toán (Phương trình \ref{eq:upper_objective}):
    \begin{equation}
        r = - \frac{J(\mathbf{x})}{10^6} = - \frac{\alpha \big[C_{\text{inv}}(\mathbf{x}) + C_{\text{op}}^*(\mathbf{x})\big] + \beta \cdot S_{\text{total}}(\mathbf{x})}{10^6}
    \end{equation}
    Việc chia cho $10^6$ giúp chuẩn hóa thang đo của phần thưởng (từ hàng tỷ USD về mức một chữ số), giúp bộ tối ưu hóa Adam trong mạng nơ-ron hoạt động ổn định và không bị nổ gradient (gradient explosion).
\end{itemize}

% ================================================================
\section{Thiết kế hệ thống và Quy trình thực thi phần mềm (Pipeline)}
% ================================================================

Để hiện thực hóa mô hình toán học trên thành một hệ thống mô phỏng và tối ưu hóa hoàn chỉnh, đề tài thiết kế một cấu trúc phần mềm (Software Pipeline) tự động với các phân hệ (modules) độc lập:

\begin{enumerate}
    \item \textbf{Phân hệ Dữ liệu (Data Module):} Xử lý dữ liệu thô (chuỗi thời gian phụ tải, tham số mạng lưới) thành các cấu trúc dữ liệu đối tượng (\texttt{SystemData}, \texttt{ZonalData}). Tích hợp bộ sinh kịch bản ngẫu nhiên (\texttt{ScenarioGenerator}) để tạo ra đa dạng các mẫu thời tiết và phụ tải theo mô hình toán học tích hợp nhiễu (noise addition).
    \item \textbf{Phân hệ Tầng dưới (Lower Level Module):} Đóng vai trò giải bài toán LP (Economic Dispatch). Phân hệ này sử dụng thư viện \texttt{scipy.optimize.linprog} với backend là bộ giải \textbf{HiGHS} -- một trong những bộ giải mã nguồn mở tốt nhất hiện nay cho LP. Bằng cách chia nhỏ 8784 giờ thành các khối (batches) hoặc giải tuần tự, hệ thống đảm bảo tiêu thụ bộ nhớ tối thiểu.
    \item \textbf{Phân hệ Tầng trên (Upper Level Module):} Tích hợp các thuật toán AI. Đối với BO, thư viện \texttt{Optuna} được sử dụng để chạy thuật toán TPE. Đối với RL, thư viện \texttt{Stable-Baselines3} quản lý mạng nơ-ron Actor-Critic và thực thi việc tính toán gradient.
\end{enumerate}

\textbf{Đánh giá độ phức tạp thuật toán:} Với hệ thống 3 vùng, mỗi giờ vận hành cần giải một bài toán LP có $N_{\text{var}} = N_{\text{gen}} + N_{\text{lines}} + N_{\text{zones}}$ biến. Khi chạy mô phỏng ngẫu nhiên (ví dụ 5 kịch bản Monte Carlo cho 8784 giờ), một lần đánh giá hàm mục tiêu ở tầng trên yêu cầu giải $5 \times 8784 = 43,920$ bài toán LP. Sự kết hợp giữa bộ giải HiGHS siêu tốc và số lượng lần đánh giá giới hạn thông minh của Bayesian Optimization/RL chính là điểm tựa kỹ thuật giúp toàn bộ hệ thống khả thi trong thời gian chạy thực tế.

"""

target_str = r"\vspace{1cm}"
if target_str in content:
    content = content.replace(target_str, new_content + target_str)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)
    print("Added new sections successfully.")
else:
    print("Target string not found!")

