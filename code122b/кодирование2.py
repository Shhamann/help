import math

y=input('кодирование чего? информации/звука/изображения')
if y==('информации'):
    x=input('чё неизвестно(информ. вес символа-i, информ. вес сообщения-I, количество символов в сообщении-K, мощность алфавита-N)? Если неизвестно что-то ещё, то когда будут спрашивать значения пиши 0')
    if x==('i'):
        I=int(input('I=?'))
        x=input('биты,байты,гигабайты,килобайты?(напиши слово)')
        if x==('байты'):
            I=I*8
        if x==('гигабайты'):
            I=I*8589934592
        if x==('килобайты'):
            I=I*8192
        K=int(input('K=?'))
        i=I//K
        if I==0 or K==0:
            N=int(input('N=?'))
        z=input('биты,байты,гигабайты,килобайты?(напиши слово)')
        if z==('биты'):
            N=N
        if z==('байты'):
            N=N*8
        if z==('гигабайты'):
            N=N*8589934592
        if z==('килобайты'):
            N=N*8192
            i=math.log2(N)
        print(i,' бит')
    if x==('I'):
        i=int(input('i=?'))
        r=input('биты,байты,гигабайты,килобайты?(напиши слово)')
        if r==('биты'):
            i=i
        if r==('байты'):
            i=i*8
        if r==('гигабайты'):
            i=i*8589934592
        if r==('килобайты'):
            i=i*8192
        K=int(input('K=?'))
        if  i==0:
            N=int(input('N=?'))
            y=input('биты,байты,гигабайты,килобайты?(напиши слово)')
            if y==('биты'):
                N=N
            if y==('байты'):
                N=N*8
            if y==('гигабайты'):
                N=N*8589934592
            if y==('килобайты'):
                N=N*8192
            i=math.log2(N)
        I=K*i
        print(I,' бит')
    if x==('K'):
        i=int(input('i=?'))
        t=input('биты,байты,гигабайты,килобайты?(напиши слово)')
        if t==('биты'):
            i=i
        if t==('байты'):
            i=i*8
        if t==('гигабайты'):
            i=i*8589934592
        if t==('килобайты'):
            i=i*8192
        I=int(input('I=?'))
        b=input('биты,байты,гигабайты,килобайты?(напиши слово)')
        if b==('байты'):
            I=I*8
        if b==('гигабайты'):
            I=I*8589934592
        if b==('килобайты'):
            I=I*8192
        if i==0:
            N=int(input('N=?'))
            n=input('биты,байты,гигабайты,килобайты?(напиши слово)')
            if n==('биты'):
                N=N
            if n==('байты'):
                N=N*8
            if n==('гигабайты'):
                N=N*8589934592
            if n==('килобайты'):
                N=N*8192
            i=math.log2(N)
        K=I//i
        print(K)
    if x==('N'):
        i=int(input('i=?'))
        p=input('биты,байты,гигабайты,килобайты?(напиши слово)')
        if p==('биты'):
            i=i
        if p==('байты'):
            i=i*8
        if p==('гигабайты'):
            i=i*8589934592
        if p==('килобайты'):
            i=i*8192
        if i==0:
            I=int(input('I=?'))
            o=input('биты,байты,гигабайты,килобайты?(напиши слово)')
            if o==('биты'):
                I=I
            if o==('байты'):
                I=I*8
            if o==('гигабайты'):
                I=I*8589934592
            if o==('килобайты'):
                I=I*8192
            K=int(input('K=?'))
            i=I//K
        N=2**i
        print(N,' бит')
elif y==('звука'):
    x=input('чё неизвестно(частота дискретизации-H, шаг дискретизации-T, битовая глубина кодирования-b, количество уровней квантования звука-K, количество произведённый измерений звукового сигнала-N, объём файла-I, время записи звука-t)? Если неизвестно 2 и более величины, то когда их будут спрашивать пиши 0')
    if x==('H'):
        N = int(input('N=?'))
        T = int(input('T=?'))
        l = input('секунды или минуты? Пиши слово с мелкой буквы')
        if l == ('минуты'):
            T = T * 60
        if N==0:
            b = int(input('b=?'))
            x = input('биты,байты,гигабайты,килобайты?(напиши слово)')
            if x == ('байты'):
                b = b * 8
            if x == ('гигабайты'):
                b = b * 8589934592
            if x == ('килобайты'):
                b = b * 8192
            I = int(input('I=?'))
            x = input('биты,байты,гигабайты,килобайты?(напиши слово)')
            if x == ('байты'):
                I = I * 8
            if x == ('гигабайты'):
                I = I * 8589934592
            if x == ('килобайты'):
                I = I * 8192
            t = int(input('t=?'))
            y=input('секунды или минуты? Пиши слово с мелкой буквы')
            if y==('минуты'):
                t=t*60
            if b==0:
                K = int(input('K=?'))
                b=log2(K)
            H=I/(t*b)
            print(H,' Гц')
        H=N//T
        print(H,' Гц')
    elif x==('t'):
        H = int(input('H=?'))
        x=input('назови точные еденицы измерения. Гц, гГц, кГц, МГц?')
        if x==('гГц'):
            H=H*100
        if x==('кГц'):
            H=H*1000
        if x==('МГц'):
            H=H*1000000
        b = int(input('b=?'))
        x = input('биты,байты,гигабайты,килобайты?(напиши слово)')
        if x == ('байты'):
            b = b * 8
        if x == ('гигабайты'):
            b = b * 8589934592
        if x == ('килобайты'):
            b = b * 8192
        I = int(input('I=?'))
        x = input('биты,байты,гигабайты,килобайты?(напиши слово)')
        if x == ('байты'):
            I = I * 8
        if x == ('гигабайты'):
            I = I * 8589934592
        if x == ('килобайты'):
            I = I * 8192
        if H==0:
            N = int(input('N=?'))
            T = int(input('T=?'))
            l = input('секунды или минуты? Пиши слово с мелкой буквы')
            if l == ('минуты'):
                T = T * 60
            H=N/T
        elif b==0:
            K = int(input('K=?'))
            b=log2(K)
        t=I//(H*b)
        print(t,' секунд')
    elif x==('N'):
        T = int(input('T=?'))
        l = input('секунды или минуты? Пиши слово с мелкой буквы')
        if l == ('минуты'):
            T = T * 60
        H = int(input('H=?'))
        x = input('назови точные еденицы измерения. Гц, гГц, кГц, МГц?')
        if x == ('гГц'):
            H = H * 100
        if x == ('кГц'):
            H = H * 1000
        if x == ('МГц'):
            H = H * 1000000
        N=H*T
        print(N)
    elif x==('K'):
        b = int(input('b=?'))
        x = input('биты,байты,гигабайты,килобайты?(напиши слово)')
        if x == ('байты'):
            b = b * 8
        if x == ('гигабайты'):
            b = b * 8589934592
        if x == ('килобайты'):
            b = b * 8192
        if b==0:
            H = int(input('H=?'))
            x = input('назови точные еденицы измерения. Гц, гГц, кГц, МГц?')
            if x == ('гГц'):
                H = H * 100
            if x == ('кГц'):
                H = H * 1000
            if x == ('МГц'):
                H = H * 1000000
            I = int(input('I=?'))
            x = input('биты,байты,гигабайты,килобайты?(напиши слово)')
            if x == ('байты'):
                I = I * 8
            if x == ('гигабайты'):
                I = I * 8589934592
            if x == ('килобайты'):
                I = I * 8192
            t = int(input('t=?'))
            p = input('секунды или минуты? Пиши слово с мелкой буквы')
            if p == ('минуты'):
                t = t * 60
            if H==0:
                T = int(input('T=?'))
                l = input('секунды или минуты? Пиши слово с мелкой буквы')
                if l == ('минуты'):
                    T = T * 60
                N = int(input('N=?'))
                H=N//T
        b=I//(H*t)
        K=2**b
        print(K)
    elif x==('T'):
        H = int(input('H=?'))
        x = input('назови точные еденицы измерения. Гц, гГц, кГц, МГц?')
        if x == ('гГц'):
            H = H * 100
        if x == ('кГц'):
            H = H * 1000
        if x == ('МГц'):
            H = H * 1000000
        N = int(input('N=?'))
        if H==0:
            I = int(input('I=?'))
            x = input('биты,байты,гигабайты,килобайты?(напиши слово)')
            if x == ('байты'):
                I = I * 8
            if x == ('гигабайты'):
                I = I * 8589934592
            if x == ('килобайты'):
                I = I * 8192
            t = int(input('t=?'))
            p = input('секунды или минуты? Пиши слово с мелкой буквы')
            if p == ('минуты'):
                t = t * 60
            b = int(input('b=?'))
            x = input('биты,байты,гигабайты,килобайты?(напиши слово)')
            if x == ('байты'):
                b = b * 8
            if x == ('гигабайты'):
                b = b * 8589934592
            if x == ('килобайты'):
                b = b * 8192
            H=I//(b*t)
        T=N/H
        print(T,' секунды')
    elif x==('b'):
        K = int(input('K=?'))
        if K==0:
            I = int(input('I=?'))
            x = input('биты,байты,гигабайты,килобайты?(напиши слово)')
            if x == ('байты'):
                I = I * 8
            if x == ('гигабайты'):
                I = I * 8589934592
            if x == ('килобайты'):
                I = I * 8192
            t = int(input('t=?'))
            l = input('секунды или минуты? Пиши слово с мелкой буквы')
            if l == ('минуты'):
                t = t * 60
            H = int(input('H=?'))
            x = input('назови точные еденицы измерения. Гц, гГц, кГц, МГц?')
            if x == ('гГц'):
                H = H * 100
            if x == ('кГц'):
                H = H * 1000
            if x == ('МГц'):
                H = H * 1000000
            if H==0:
                T = int(input('T=?'))
                l = input('секунды или минуты? Пиши слово с мелкой буквы')
                if l == ('минуты'):
                    T = T * 60
                N = int(input('N=?'))
                H=N//T
            b=I/(H*t)
            print(b)
        b=math.log2(K)
        print(b)
    elif x==('I'):
        t = int(input('t=?'))
        v = input('секунды или минуты? Пиши слово с мелкой буквы')
        if v == ('минуты'):
            t = t * 60
        H = int(input('H=?'))
        x = input('назови точные еденицы измерения. Гц, гГц, кГц, МГц?')
        if x == ('гГц'):
            H = H * 100
        if x == ('кГц'):
            H = H * 1000
        if x == ('МГц'):
            H = H * 1000000
        b = int(input('b=?'))
        x = input('биты,байты,гигабайты,килобайты?(напиши слово)')
        if x == ('байты'):
            b = b * 8
        if x == ('гигабайты'):
            b = b * 8589934592
        if x == ('килобайты'):
            b = b * 8192
        if H==0:
            T = int(input('T=?'))
            l = input('секунды или минуты? Пиши слово с мелкой буквы')
            if l == ('минуты'):
                T = T * 60
            N = int(input('N=?'))
            H=N/T
        if b==0:
            K = int(input('K=?'))
            b=math.log2(K)
        I=H*t*b
        print(I)
elif y==('изображения'):
    x=input('что неизвестно(количество оттенков-K, битовая глубина кодирования-b)?')
    if x==('b'):
        K=int(input('K=?'))
        b=log2(K)
        print(b)
    if x==('K'):
        b=int(input('b=?'))
        K=2**b
        print(K)
