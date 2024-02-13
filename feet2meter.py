def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):
	# Здесь будет ваш код
    return float(v[:-2]) / 3.280858935761181

main()
