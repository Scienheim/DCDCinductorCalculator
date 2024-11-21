import tkinter as tk
from tkinter import messagebox


# 计算电感的函数
def calculate_inductor():
    try:
        # 获取输入的值
        V_in = float(entry_V_in.get())
        V_out = float(entry_V_out.get())
        I_out = float(entry_I_out.get())
        f_s_kHz = float(entry_f_s_kHz.get())  # 开关频率 (kHz)
        gamma_min = float(entry_gamma_min.get())  # 最小纹波系数
        gamma_max = float(entry_gamma_max.get())  # 最大纹波系数

        # 将开关频率从 kHz 转换为 Hz
        f_s = f_s_kHz * 1000  # 开关频率 (Hz)

        # 计算电流纹波
        delta_I_L_min = gamma_min * I_out  # 最小纹波
        delta_I_L_max = gamma_max * I_out  # 最大纹波

        # 根据选择的公式来计算电感
        if selected_circuit.get() == "Buck":
            L_min = (V_out * (V_in - V_out)) / (f_s * delta_I_L_min * V_in)
            L_max = (V_out * (V_in - V_out)) / (f_s * delta_I_L_max * V_in)
        elif selected_circuit.get() == "Boost":
            L_min = (V_in * (V_out - V_in)) / (f_s * delta_I_L_min * V_out)
            L_max = (V_in * (V_out - V_in)) / (f_s * delta_I_L_max * V_out)
        elif selected_circuit.get() == "Buck-Boost":
            L_min = (V_in * (V_out - V_in)) / (f_s * delta_I_L_min * V_out)
            L_max = (V_in * (V_out - V_in)) / (f_s * delta_I_L_max * V_out)

        # 将电感值转换为 μH
        L_min_uH = L_min * 1e6  # 电感最小值 (μH)
        L_max_uH = L_max * 1e6  # 电感最大值 (μH)

        # 显示计算结果
        result_label.config(text=f"电感最小值：{L_min_uH:.6f} μH\n电感最大值：{L_max_uH:.6f} μH")
    except ValueError:
        messagebox.showerror("输入错误", "请输入有效的数字！")
    except ZeroDivisionError:
        messagebox.showerror("计算错误", "输入参数导致除数为零，请检查输入值！")


# 创建窗口
root = tk.Tk()
root.title("电感计算器")

# 设置窗口大小
root.geometry("600x450")

# 使窗口大小可调整，并且控件大小会自动调整
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)
root.grid_columnconfigure(2, weight=2)
root.grid_columnconfigure(3, weight=1)

# 电路类型选择
selected_circuit = tk.StringVar(value="Buck")
label_circuit = tk.Label(root, text="选择电路类型:")
label_circuit.grid(row=0, column=0, padx=10, pady=10, sticky="e")

radio_buck = tk.Radiobutton(root, text="Buck", variable=selected_circuit, value="Buck")
radio_buck.grid(row=0, column=1, padx=10, pady=10, sticky="w")

radio_boost = tk.Radiobutton(root, text="Boost", variable=selected_circuit, value="Boost")
radio_boost.grid(row=0, column=2, padx=10, pady=10, sticky="w")

radio_buck_boost = tk.Radiobutton(root, text="Buck-Boost", variable=selected_circuit, value="Buck-Boost")
radio_buck_boost.grid(row=0, column=3, padx=10, pady=10, sticky="w")

# 输入框标签和输入框
label_V_in = tk.Label(root, text="输入电压 (V_in):")
label_V_in.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_V_in = tk.Entry(root)
entry_V_in.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

label_V_out = tk.Label(root, text="输出电压 (V_out):")
label_V_out.grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_V_out = tk.Entry(root)
entry_V_out.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

label_I_out = tk.Label(root, text="负载电流 (I_out):")
label_I_out.grid(row=3, column=0, padx=10, pady=10, sticky="e")
entry_I_out = tk.Entry(root)
entry_I_out.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

label_f_s_kHz = tk.Label(root, text="开关频率 (f_s) kHz:")
label_f_s_kHz.grid(row=4, column=0, padx=10, pady=10, sticky="e")
entry_f_s_kHz = tk.Entry(root)
entry_f_s_kHz.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

label_gamma_min = tk.Label(root, text="最小纹波系数 (γ_min):")
label_gamma_min.grid(row=5, column=0, padx=10, pady=10, sticky="e")
entry_gamma_min = tk.Entry(root)
entry_gamma_min.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

label_gamma_max = tk.Label(root, text="最大纹波系数 (γ_max):")
label_gamma_max.grid(row=6, column=0, padx=10, pady=10, sticky="e")
entry_gamma_max = tk.Entry(root)
entry_gamma_max.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

# 结果标签
result_label = tk.Label(root, text="电感最小值和最大值：")
result_label.grid(row=7, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# 计算按钮
calculate_button = tk.Button(root, text="计算电感", command=calculate_inductor)
calculate_button.grid(row=8, column=0, columnspan=4, pady=20, sticky="nsew")

# 运行程序
root.mainloop()
