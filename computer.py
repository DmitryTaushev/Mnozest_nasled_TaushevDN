class PowerUnit:
    def __init__(self,power):
        self.power = power

    def power_need(self):
        if self.power < 400:
            return f'Недостаточно напряжения {self.power} Bт'
        elif self.power >1000:
           return f"Переизбыток напряжения {self.power} Bт"
        elif ((self.power >= 400) and (self.power <= 1000)):
            return f"Достаточно напряжения {self.power} Bт"

class Motherboard:
    def __init__(self,chipset,power):
        self.power = power
        self.chipset = chipset

    def power_separate(self):
        cpu_power = (self.power*40)/100
        video_power = (self.power*60)/100
        return f"{cpu_power} Вт ушло на питание процессора, {video_power} Вт ушло на питание видео карты"

class CPU:
    def __init__(self,cloak_freq,core_num):
        self.cloak_freq = cloak_freq
        self.core_num = core_num

    def turboboost(self,mode):
        if mode == "ON":
            return "Турбо режим включен"
        elif mode == "OFF":
            return "Турбо режим выключен"

    def get_cloak(self):
        return self.cloak_freq

    def get_core(self):
        return self.core_num


class RAM:
    def __init__(self,memory,frequency):
        self.memory = memory
        self.frequency = frequency

    def RAM_work(self):
        time = self.memory/self.frequency
        return f'Время записи информации {time}'

class SSD:
    def __init__(self,ssd_memory):
        self.ssd_memory = ssd_memory

    def memory_change(self,direct,inform):
        dict_inform = {direct:inform}
        return f'Записанная информация {dict_inform}'

class VideoCard:
    def __init__(self,model,vc_memory):
        self.model = model
        self.vc_memory = vc_memory

    def get_model(self):
        return self.model

    def get_vc_memory(self):
        return self.vc_memory


class Computer(PowerUnit,Motherboard,CPU,RAM,SSD,VideoCard):
    def __init__(self,power,chipset, cloak_freq,core_num,memory,frequency,ssd_memory,model,vc_memory):
        PowerUnit.__init__(self,power)
        Motherboard.__init__(self,chipset,power)
        CPU.__init__(self,cloak_freq,core_num)
        RAM.__init__(self,memory,frequency)
        SSD.__init__(self,ssd_memory)
        VideoCard.__init__(self,model,vc_memory)

comp = Computer(500,"NVIDIA",1.8,8,32000,400,2000,'RTX4080',16000)

print(comp.power_need())
print(comp.power_separate())
print(comp.turboboost('ON'))
print(comp.RAM_work())
print(comp.memory_change('Новая папка','computer.py'))
print(comp.get_model())
print(comp.get_vc_memory())





