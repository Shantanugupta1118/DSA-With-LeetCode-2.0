class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        factors = {2: 0, 3: 0, 5: 0, 7: 0}
        for p in [2, 3, 5, 7]:
            while t % p == 0:
                factors[p] += 1
                t //= p
        
        if t > 1:
            return "-1"

        def get_min_digits_needed(f2, f3, f5, f7):
            c9 = f3 // 2
            rem_3 = f3 % 2

            c8 = f2 // 3
            rem_2 = f2 % 3

            c6 = 0
            if rem_2 > 0 and rem_3 > 0:
                c6 = 1
                rem_2 -= 1
                rem_3 -= 1

            c4 = rem_2 // 2
            rem_2 %= 2

            return c9 + c8 + c6 + c4 + rem_2 + rem_3 + f5 + f7

        def fill_suffix(length, f2, f3, f5, f7):
            c9 = f3 // 2
            rem_3 = f3 % 2

            c8 = f2 // 3
            rem_2 = f2 % 3

            c6 = 0
            if rem_2 > 0 and rem_3 > 0:
                c6 = 1
                rem_2 -= 1
                rem_3 -= 1

            c4 = rem_2 // 2
            rem_2 %= 2

            c2, c3, c5, c7 = rem_2, rem_3, f5, f7

            total_non_ones = c9 + c8 + c6 + c5 + c4 + c3 + c2 + c7
            if total_non_ones > length:
                return None

            c1 = length - total_non_ones
            res = (['1'] * c1 + ['2'] * c2 + ['3'] * c3 + ['4'] * c4 + 
                   ['5'] * c5 + ['6'] * c6 + ['7'] * c7 + ['8'] * c8 + ['9'] * c9)
            return "".join(res)

        n = len(num)
        
        first_zero = num.find('0')
        
        valid_prefix_len = first_zero if first_zero != -1 else n
        pref_factors = [{2: 0, 3: 0, 5: 0, 7: 0}]
        for i in range(valid_prefix_len):
            d = int(num[i])
            cur = pref_factors[-1].copy()
            temp = d
            for p in [2, 3, 5, 7]:
                while temp > 0 and temp % p == 0:
                    cur[p] += 1
                    temp //= p
            pref_factors.append(cur)

        if first_zero == -1:
            c2 = max(0, factors[2] - pref_factors[n][2])
            c3 = max(0, factors[3] - pref_factors[n][3])
            c5 = max(0, factors[5] - pref_factors[n][5])
            c7 = max(0, factors[7] - pref_factors[n][7])
            if c2 == 0 and c3 == 0 and c5 == 0 and c7 == 0:
                return num

        limit = first_zero if first_zero != -1 else n - 1

        for i in range(limit, -1, -1):
            c2 = max(0, factors[2] - pref_factors[i][2])
            c3 = max(0, factors[3] - pref_factors[i][3])
            c5 = max(0, factors[5] - pref_factors[i][5])
            c7 = max(0, factors[7] - pref_factors[i][7])

            start_digit = 1 if i == first_zero else int(num[i]) + 1

            for d in range(start_digit, 10):
                d_f = {2: 0, 3: 0, 5: 0, 7: 0}
                temp = d
                for p in [2, 3, 5, 7]:
                    while temp % p == 0:
                        d_f[p] += 1
                        temp //= p

                rem_2 = max(0, c2 - d_f[2])
                rem_3 = max(0, c3 - d_f[3])
                rem_5 = max(0, c5 - d_f[5])
                rem_7 = max(0, c7 - d_f[7])

                rem_len = n - 1 - i
                if get_min_digits_needed(rem_2, rem_3, rem_5, rem_7) <= rem_len:
                    suf = fill_suffix(rem_len, rem_2, rem_3, rem_5, rem_7)
                    if suf is not None:
                        return num[:i] + str(d) + suf

        min_len = max(n + 1, get_min_digits_needed(factors[2], factors[3], factors[5], factors[7]))
        return fill_suffix(min_len, factors[2], factors[3], factors[5], factors[7])