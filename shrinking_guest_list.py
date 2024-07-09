guests = ['jesus christ', 'david bowie', 'jeff bridges']
del guests[2]
guests.append('stanley kubrick')
guests.insert(0, 'janet leigh')
guests.insert(2, 'bela lugosi')
guests.append('abraham lincoln')
print(f"Attention guests, unfortunately the new table will arrive late.  Therefore the guest list is now cut down to two.")
print(guests)
cancelled_guests = guests.pop(0)
print(f"Dear {cancelled_guests.title()}, you are no longer invited to dinner.  Apologies.")
cancelled_guests2 = guests.pop(1)
print(f"Dear {cancelled_guests2.title()}, you are no longer invited to dinner.  Apologies.")
cancelled_guests3 = guests.pop(1)
print(f"Dear {cancelled_guests3.title()}, you are no longer invited to dinner.  Apologies.")
cancelled_guests4 = guests.pop(1)
print(f"Dear {cancelled_guests4.title()}, you are no longer invited to dinner.  Apologies.")
print(guests)
print(f"Dear {guests[0].title()}, you are still invited to dinner tonight.  You and the other guest will have a lot to talk about.")
print(f"Dear {guests[1].title()}, you are still invited to dinner tonight.  You and the other guest will have a lot to talk about.")
del guests[0]
del guests[0]
print(guests)