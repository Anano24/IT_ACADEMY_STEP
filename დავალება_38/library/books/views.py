from django.shortcuts import render, redirect

# Create your views here.


books = [
    {'id': 1, 'title': 'ნუ მოკლავ ჯაფარას', 'author': 'ჰარპერ ლი', 'img_link': 'https://sulakauri.b-cdn.net/wp-content/uploads/2020/02/nu-moklav-japharas.jpg',  'description': 'ცნობილი მწერლის, ჰარპერ ლის  რომანი “ნუ მოკლავ ჯაფარას’ თავის დროზე სამართლიანად აღიარეს ყველაზე ჰუმანურ ამერიკულ ნაწარმოებად. დიდი დეპრესიის პერიოდში ალაბამის შტატის ერთ პატარა ქალაქში განვითარებული, 6 წლის გოგონას, ჯინ ლუიზა ფინჩის თვალით დანახული მოვლენები თანამედროვე მკითხველსაც ასწავლის, რა არის კარგი და რა – ცუდი, რომ ადამიანური წარმოდგენები ხშირად იცვლება, რომ ამქვეყნად ყველაზე მნიშვნელოვანი სიყვარული და სამართლიანობაა.'},
    {'id': 2, 'title': 'კაფკა პლაჟზე', 'author': 'ჰარუკი მურაკამი', 'img_link':'https://sulakauri.b-cdn.net/wp-content/uploads/2022/11/kaphka-plazhze.webp', 'description': 'ჰარუკი მურაკამის რომანი „კაფკა პლაჟზე“ 2002 წელს გამოიცა და სხვადასხვა პრემიებთან ერთად, 2005 წელს ფრანკფურტის წიგნის ბაზრობაზე საუკეთესო ახალგაზრდული წიგნის ჯილდოც მოიპოვა.'},
    {'id': 3, 'title': 'ილიადა', 'author': 'ჰომეროსი', 'img_link':'https://sulakauri.b-cdn.net/wp-content/uploads/2020/02/iliada.jpg', 'description':'როგორც უნდა აიგოს „თავისუფალ ხელოვნებათა“ კანონი, მაინც ვერავინ აუვლის გვერდს პირველ ევროპელ ავტორს, ჰომეროსს… იგი ამგვარ სიაში, როგორც წესი, პირველია. პირველი წასაკითხი წიგნებიც ჰომეროსის პოემები „ილიადა“ და „ოდისეაა“.'},
    {'id': 4, 'title': 'ნაწყვდიადევს', 'author': 'ჰარუკი მურაკამი', 'img_link':'https://sulakauri.b-cdn.net/wp-content/uploads/2020/07/natsqhvdiadevs.jpg', 'description':'რომანის ყველა ამბავი ერთ ღამეში ხდება. უზარმაზარ მეგაპოლისში ადამიანები შემთხვევით ხვდებიან ერთმანეთს, უყვარდებათ, შორდებიან და ისევ ხვდებიან, როცა წყვდიადი უკან იხევს.'},
    {'id': 5, 'title': 'შაშვი შაშვი მაყვალი', 'author': 'თამთა მელაშვილი', 'img_link':'https://sulakauri.b-cdn.net/wp-content/uploads/2021/01/shashvi-shashvi-maqhvali.jpg', 'description':'შუახნის, მარტოხელა ქალი ეთერო პატარა ქალაქის მკვიდრია და თავისსავე მაღაზიაში მუშაობს. მის ერთფეროვან, უშფოთველ ცხოვრებას თითქოს არაფერი ემუქრება, მაგრამ ერთ დღეს, მოულოდნელი ინციდენტი შეემთხვევა და მისი დალაგებული ცხოვრება თავდაყირა დგება. სიკვდილის შიშით შეძრული ქალი ისეთ გადაწყვეტილებას იღებს, სხვა დროს რომ ვერაფრით გაბედავდა და მოულოდნელ სასიყვარულო თავგადასავალში ეხვევა.'},
    {'id': 6, 'title': 'ვარდის სურნელი', 'author': 'ზაზა ბურჭულაძე', 'img_link':'https://sulakauri.b-cdn.net/wp-content/uploads/2022/05/vardis-surneli.webp', 'description':'„ვარდის სურნელი“ – ესაა სულისშემძვრელი რომანი სიტყვებზე. რომანი-ლაბირინთი, რომელიც გულგრილს არავის დატოვებს. თუ ნიცშეს „ზარატუსტრა“ არის წიგნი ყველასთვის და არავისთვის, „ვარდის სურნელი“ არის წიგნი არავისთვის და ყველასთვის. და ეს არ არის სიტყვების თამაში. სიტყვების თამაშია თვითონ რომანი – წიგნი-გამოწვევა, რომლის არომატიც არასდროს არაფერში აგერევა.'},
]


def homepage(request):
    return render(request, 'index.html', {'books': books})



def aboutpage(request):
    return render(request, 'about.html')



def book_detail(request, id):
    one_book = None

    for book in books:
        if book['id'] == id:
            one_book = book
            break
    
    return render(request, 'book_detail.html', {'one_book': one_book})



def delete_book(request, id):
    book_for_delete = None

    for book in books:
        if book['id'] == id:
            book_for_delete = book
            break
    
    books.remove(book_for_delete)
    return redirect('books:homepage')

