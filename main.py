import tkinter as tk
from tkinter import messagebox

# 计算电感的函数
def calculate_inductor():
    try:
        # 获取输入的值
        V_in = float(entry_V_in.get())
        V_out = float(entry_V_out.get())
        I_out = float(entry_I_out.get())
        f_s = float(entry_f_s.get())
        delta_I_L = float(entry_delta_I_L.get())

        # 根据选择的公式来计算电感
        if selected_circuit.get() == "Buck":
            L = (V_out * (V_in - V_out)) / (f_s * delta_I_L * V_in)
        elif selected_circuit.get() == "Boost":
            L = (V_in * (V_out - V_in)) / (f_s * delta_I_L * V_out)
        elif selected_circuit.get() == "Buck-Boost":
            L = (V_in * (V_out - V_in)) / (f_s * delta_I_L * V_out)

        # 显示计算结果
        result_label.config(text=f"计算得到的电感值：{L:.6f} H")
    except ValueError:
        messagebox.showerror("输入错误", "请输入有效的数字！")
    except ZeroDivisionError:
        messagebox.showerror("计算错误", "输入参数导致除数为零，请检查输入值！")


# 创建窗口
root = tk.Tk()
root.title("电感计算器")

# 设置窗口大小
root.geometry("400x400")

# 电路类型选择
selected_circuit = tk.StringVar(value="Buck")
label_circuit = tk.Label(root, text="选择电路类型:")
label_circuit.grid(row=0, column=0, padx=10, pady=5)

radio_buck = tk.Radiobutton(root, text="Buck", variable=selected_circuit, value="Buck")
radio_buck.grid(row=0, column=1, padx=10, pady=5)

radio_boost = tk.Radiobutton(root, text="Boost", variable=selected_circuit, value="Boost")
radio_boost.grid(row=0, column=2, padx=10, pady=5)

radio_buck_boost = tk.Radiobutton(root, text="Buck-Boost", variable=selected_circuit, value="Buck-Boost")
radio_buck_boost.grid(row=0, column=3, padx=10, pady=5)

# 输入框标签和输入框
label_V_in = tk.Label(root, text="输入电压 (V_in):")
label_V_in.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_V_in = tk.Entry(root)
entry_V_in.grid(row=1, column=1, padx=10, pady=5)

label_V_out = tk.Label(root, text="输出电压 (V_out):")
label_V_out.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_V_out = tk.Entry(root)
entry_V_out.grid(row=2, column=1, padx=10, pady=5)

label_I_out = tk.Label(root, text="负载电流 (I_out):")
label_I_out.grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_I_out = tk.Entry(root)
entry_I_out.grid(row=3, column=1, padx=10, pady=5)

label_f_s = tk.Label(root, text="开关频率 (f_s):")
label_f_s.grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_f_s = tk.Entry(root)
entry_f_s.grid(row=4, column=1, padx=10, pady=5)

label_delta_I_L = tk.Label(root, text="电流纹波 (ΔI_L):")
label_delta_I_L.grid(row=5, column=0, padx=10, pady=5, sticky="e")
entry_delta_I_L = tk.Entry(root)
entry_delta_I_L.grid(row=5, column=1, padx=10, pady=5)

# 结果标签
result_label = tk.Label(root, text="计算得到的电感值：")
result_label.grid(row=6, column=0, columnspan=4, padx=10, pady=20)

# 计算按钮
calculate_button = tk.Button(root, text="计算电感", command=calculate_inductor)
calculate_button.grid(row=7, column=0, columnspan=4, pady=10)

# 运行程序
root.mainloop()
