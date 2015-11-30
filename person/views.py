from django.template import RequestContext
from models import Teacher,Yonghu,Log,Student
from django.shortcuts import render_to_response

from django.http import HttpResponseRedirect
def login(request):
    if request.method == "POST":
        name=request.POST['username']
        d=RequestContext(request,{"number":name})
        password=request.POST['password']
        p=Yonghu.objects.filter(Number = name)
        if len(p)!=0:   
            for i in p:
                if password==i.Password:
                    if i.Leibie=="teacher":
                        q=Teacher.objects.filter(Number=i.Number)
                        if len(q)!=0:
                            for j in q:
                                c=RequestContext(request,{"teacher":j})
                                return render_to_response("sunyan4.html",c)
                        else:
                            return render_to_response("empty.html",d)
                    elif i.Leibie=="student":
                        q=Student.objects.filter(Number=i.Number)
                        if len(q)!=0:
                            for j in q:
                                c=RequestContext(request,{"student":j})
                                return render_to_response("sunyan1.html",c)
                        else:
                            return render_to_response("empty.html",d)
                else:
                    return render_to_response("failure.html")
        else:
            return render_to_response("failure.html")
    else:
        return render_to_response("login.html")
def register(request):
     if request.POST:
        post = request.POST
        new = Yonghu(
            Number = post["user"],
            Password = post["Password"],
            Leibie= post["Leibie"],
            )    
        new.save()
     return render_to_response("register.html")
def create(request):
    ID = request.GET["id"]
    d=RequestContext(request,{"number":ID})
    p=Yonghu.objects.filter(Number = ID)
    for i in p:
        if i.Leibie=="teacher":
            if request.POST:
                post = request.POST
                new_teacher = Teacher(
                    Name = post["Name"],
                    Profession = post["Profession"],
                    Information = post["Information"],
                    Foundation = post["Foundation"],
                    Research = post["Research"],
                    Tel = post["Tel"],
                    Work = post["Work"],
                    Education = post["Education"],
                    Position = post["Position"],
                    Rongyu = post["Rongyu"],
                    Jianzhi = post["Jianzhi"],
                    Rfield = post["Rfield"],
                    Number = Yonghu.objects.get(Number=ID),
                    )    
                new_teacher.save()
                c=RequestContext(request,{"teacher":new_teacher,"number":ID,})
                return render_to_response("sunyan4.html",c)
            else:
                return render_to_response("sunyan3.html")
        else:
            if request.POST:
                post = request.POST
                new_student = Student(
                    Name = post["Name"],
                    Profession = post["Profession"],
                    Tel = post["Tel"],
                    Xuenian = post["Xuenian"],
                    Number = Yonghu.objects.get(Number=ID),
                    )    
                new_student.save()
                c=RequestContext(request,{"student":new_student,"number":ID,})
                return render_to_response("sunyan1.html",c)
            else:
                return render_to_response("sunyan2.html")
def updata(request):
    ID = request.GET["id"]
    d=RequestContext(request,{"ID":ID})
    a=Yonghu.objects.get(Number = ID)
    if a.Leibie=="teacher":
        p=Teacher.objects.get(Number = ID)
        c=RequestContext(request,{"teacher":p})
        e=RequestContext(request,{"teacher":p,"ID":ID,})
        if request.POST:
            post = request.POST
            p.Name = post["Name"]
            p.Profession = post["Profession"]
            p.Information = post["Information"]
            p.Foundation = post["Foundation"]
            p.Research = post["Research"]
            p.Work = post["Work"]
            p.Tel = post["Tel"]
            p.Education = post["Education"]
            p.Position = post["Position"]
            p.Rongyu = post["Rongyu"]
            p.Jianzhi = post["Jianzhi"]
            p.Rfield = post["Rfield"]
            p.Number= Yonghu.objects.get(Number= ID)
            p.save()
            return render_to_response("sunyan4.html",c)
        else:
            return render_to_response("sunyan5.html",e)
    else:
        p=Student.objects.get(Number = ID)
        c=RequestContext(request,{"student":p})
        e=RequestContext(request,{"student":p,"ID":ID,})
        if request.POST:
            post = request.POST
            p.Name = post["Name"]
            p.Profession = post["Profession"]
            p.Tel = post["Tel"]
            p.Xuenian= post["Xuenian"]
            p.Number= Yonghu.objects.get(Number= ID)
            p.save()
            return render_to_response("sunyan1.html",c)
        else:
            return render_to_response("sunyan7.html",e)
def search(request):
    ID = request.GET["id"]
    d=RequestContext(request,{"Number":ID})
    if request.method == "POST":
        post=request.POST['search']
        p=Teacher.objects.filter(Name = post)
        c=RequestContext(request,{"Teacher_list":p,"Number":ID,})
        return render_to_response("sunyan6.html",c)
    else:
        return render_to_response("sunyan6.html",d)
def search_event(request):
	ID = request.GET["id"]
	if "but" in request.POST:
		time = request.POST.get("but")
		monthlist = Log.objects.filter(Time = time, Number = ID)
		monthlist.delete()
		return render_to_response("search_event.html",RequestContext(request,{"ID":ID,}))
	if request.POST:
		post = request.POST
		time = post["date"]
		tmp = time.split('-')
		year = int(tmp[0])
		c = -1
		if len(tmp) > 1:
			month = int(tmp[1])
			if month < 3:
				m = month+12
				y = (year - 1) % 100
			else:
				m = month
				y=year%100
			if len(tmp) >=3:
				day = int(tmp[2])
				c = y + int(y/4) + 5 - 2 * 20 +int(26 * (m + 1) / 10) + day - 1
				c = c % 7
		else:
			month = ""
		monthlist=Log.objects.filter(Time__contains = time, Number = ID)
		return render_to_response("search_event.html", RequestContext(request,{"year":year,"month":month,"date_list":monthlist,"ID":ID,"d":c,}))
	return render_to_response("search_event.html",RequestContext(request,{"ID":ID,}))
def add_event(request):
	ID = request.GET["id"]
	if request.POST:
		post =  request.POST
		new_event = Log(
			Number = ID,
			Time = post["time"],
			Event = post["event"]
		)
		new_event.save()
		return HttpResponseRedirect("/search_event/?id="+ID)
	return render_to_response("add_event.html")
def search_event1(request):
    ID = request.GET["sousuo"]
    Number=request.GET["id"]
    if request.POST:
		post = request.POST
		time = post["date"]
		tmp = time.split('-')
		year = int(tmp[0])
		if len(tmp) > 1:
			month = int(tmp[1])
		else:
			month = ""
		# if month < 3:
			# m = month+12
			# y = (year - 1) % 100
		# else:
			# m = month
			# y=year%100
		# c = y % 100 + int(y/4) + 5 - 2 * 20 +int(26 * (m + 1) / 10) + 1 - 1
		# c = 8 - c
		monthlist=Log.objects.filter(Time__contains = time, Number = ID)
		return render_to_response("search_event1.html", RequestContext(request,{"year":year,"month":month,"date_list":monthlist,"ID":ID,"Number":Number,}))
    return render_to_response("search_event1.html",RequestContext(request,{"ID":ID,"Number":Number,}))
def fanhui(request):
    ID = request.GET["id"]
    a=Yonghu.objects.get(Number = ID)
    if a.Leibie=="teacher":
        p=Teacher.objects.filter(Number = ID)
        for i in p:
            c=RequestContext(request,{"teacher":i})
            return render_to_response("sunyan4.html",c)
    else:
        p=Student.objects.filter(Number = ID)
        for i in p:
            c=RequestContext(request,{"student":i})
            return render_to_response("sunyan1.html",c)