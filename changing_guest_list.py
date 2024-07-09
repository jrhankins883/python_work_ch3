guests = ['jesus christ', 'david bowie', 'jeff bridges']
print(f"Due to being creeped out by the other guests being supposedly dead... {guests[2].title()} will not be coming to dinner.")
del guests[2]
print(guests)

guests.append('stanley kubrick')
print(guests)
print(f"I know you're probably very busy dealing with us crazy humans but, {guests[0].title()}, you're cordially invited to dinner.")
print(f"{guests[1].title()}, aka Ziggy Stardust, you're cordially invited to dinner.")
print(f"As long as I can pick your brain about Eyes Wide Shut then, {guests[2].title()}, you're cordially invited to dinner.")

print(f"\nAttention dinner guests, I have found a bigger dinner table.  We will be seeing more guests than originally planned!")