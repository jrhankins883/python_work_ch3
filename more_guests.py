guests = ['jesus christ', 'david bowie', 'jeff bridges']
print(f"Due to being creeped out by the other guests being supposedly dead... {guests[2].title()} will not be coming to dinner.")
del guests[2]
guests.append('stanley kubrick')
print(guests)
print(f"\nAttention dinner guests, I have found a bigger dinner table.  We will be seeing more guests than originally planned!")

guests.insert(0, 'janet leigh')
guests.insert(2, 'bela lugosi')
guests.append('abraham lincoln')
print(guests)

print(f"{guests[0].title()}, you are cordially invited to dinner.  You will be asked about Alfred Hitchcock.")
print(f"I know you're probably very busy dealing with us crazy humans but, {guests[1].title()}, you're cordially invited to dinner.")
print(f"You will not be expected to wear your Dracula costume {guests[2].title()}.  We hope you'll still come to dinner!")
print(f"{guests[3].title()}, aka Ziggy Stardust, you're cordially invited to dinner.")
print(f"As long as I can pick your brain about Eyes Wide Shut then, {guests[4].title()}, you're cordially invited to dinner.")
print(f"{guests[5].title()}, you are cordially invited to dinner under the condition that you do not give any long speeches.")