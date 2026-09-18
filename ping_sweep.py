import subprocess
import platform
from concurrent.futures import ThreadPoolExecutor

def verificar_host(ip):
    # Identifica se o sistema é Windows ou Linux para ajustar o comando ping
    parametro = "-n" if platform.system().lower() == "windows" else "-c"
    comando = ["ping", parametro, "1", "-w", "100", ip]
    
    # Executa o comando ping de forma silenciosa
    resultado = subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if resultado.returncode == 0:
        print(f"[+] Host ATIVO: {ip}")
        return ip
    return None

def main():
    print("--- Verificador de Hosts Online (Ping Sweep) ---")
    rede_base = input("Digite os 3 primeiros octetos da rede (ex: 192.168.1): ")
    
    print(f"\nVarrendo a rede {rede_base}.1 até {rede_base}.254...\n")
    
    ips_para_testar = [f"{rede_base}.{i}" for i in range(1, 255)]
    
    # Executa os pings em paralelo para ser bem rápido
    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(verificar_host, ips_para_testar)
        
    print("\nVarredura concluída!")
    
    # Segura a tela aberta para você visualizar os resultados
    input("\nPressione ENTER para sair...")

if __name__ == "__main__":
    main()