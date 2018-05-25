from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from models import User, Trip, JoinedTrips
import bcrypt, time

def delete_everything(request):
    e = Trip.objects.all().delete()
    f = JoinedTrips.objects.all().delete()
    request.session["logged_user"] = []
    request.session["name"] = []
    request.session["l_id"] = []
    return redirect('/travel_buddy/main/')

def index(request):
    if "logged_user" not in request.session:
        request.session["user"] = []
        return render(request, 'travel_buddy/index.html')
    else:
        if not request.session["logged_user"]:
            return render(request, 'travel_buddy/index.html')
        else:
            owner = User.objects.filter(id=request.session["l_id"])
            ut = JoinedTrips.objects.filter(user=owner)
            x = []
            z = []
            y = JoinedTrips.objects.all()
            for a in range(0, len(ut)):
                z.append(ut[a].trip.id)
    
            for a in range(0, len(y)):
                valid = True
                for b in range(0, len(z)):
                    if y[a].trip.id == z[b]:
                        valid = False
                        break
                if valid:
                    x.append(y[a])
            context = {
                "user_trips": ut,
                "other_trips": x,
                "user": request.session["name"]
            }
            return render(request, 'travel_buddy/travels.html', context)

def register(request):
    if User.objects.validate(request):
        User.objects.create(name=request.POST["name"], 
                        username=request.POST["username"], 
                        password=request.POST["pass1"])
        messages.success(request, "Created User, please login")
    return redirect('/travel_buddy/main/')

def login(request):
    users = User.objects.filter(username=request.POST["username"])
    if len(users) > 0:
        user = users[0]
        if user.password == request.POST["pass"]:
            request.session["logged_user"] = request.POST["username"]
            request.session["name"] = user.name
            request.session["l_id"] = user.id
        else:
            messages.error(request, "Invalid password")
    else:
        messages.error(request, "Invalid username")
    return redirect('/travel_buddy/main/')

def logout(request):
    request.session["logged_user"] = []
    request.session["name"] = []
    request.session["l_id"] = []
    return redirect('/travel_buddy/main/')

def add(request):
    return render(request, 'travel_buddy/add.html')

def create(request):
    d = request.POST
    if Trip.objects.validate(request):
        owner = User.objects.get(username=request.session["logged_user"])
        Trip.objects.create(tripname=d["destination"], description=d["description"], tstartdate=d["tstartdate"], tenddate=d["tenddate"], created_by=owner)
        get_trip_id = Trip.objects.all().order_by('-created_at')[0]
        return redirect('/travel_buddy/join/'+str(get_trip_id.id)+'/')
    else:
        return redirect('/travel_buddy/travels/add/')
    return redirect('/travel_buddy/travels/')

def showtrip(request, trip_id):
    owner = Trip.objects.filter(id=trip_id)
    owner = owner[0]
    q = owner.created_by.id
    context = {
        "trip": Trip.objects.get(id=trip_id),
        "joined": JoinedTrips.objects.filter(trip=trip_id).exclude(user=q)
    }
    return render(request, 'travel_buddy/destination.html', context)

def join(request, trip_id):
    t = Trip.objects.filter(id=trip_id)
    u = User.objects.filter(username=request.session["logged_user"])
    q = JoinedTrips.objects.filter(trip=t, user=u,)
    if len(q) < 1:
        u = u[0]
        t = t[0]
        JoinedTrips.objects.create(trip=t, user=u)
    else:
        messages.error(request, "You already joined that trip")
    return redirect('/travel_buddy/travels/')