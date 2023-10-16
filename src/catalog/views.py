from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models          import *



def create_post(request):
    """
    Handle the creation of a post.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.method == 'GET':
        # Create the context with the necessary forms
        context = {
            'form': siteForm(),
            'hvac': hvacForm(),
            'battery': batteryForm(),
            'relion': relionForm(),
            'contacts': contactsForm(),
        }
        # Render the post form template with the context
        return render(request, 'post_form.html', context=context)
    elif request.method == 'POST':
        # Create the forms with the POST data
        form = siteForm(request.POST)
        hvac = hvacForm(request.POST)
        battery = batteryForm(request.POST)
        relion = relionForm(request.POST)
        contacts = contactsForm(request.POST)

        # Save the form data and redirect to 'All Sites' if valid
        if form.is_valid():
            form.save()
            return redirect('All Sites')
        elif hvac.is_valid():
            hvac.save()
            return redirect('All Sites')
        elif battery.is_valid():
            battery.save()
            return redirect('All Sites')
        elif relion.is_valid():
            relion.save()
            return redirect('All Sites')
        elif contacts.is_valid():
            contacts.save()
            return redirect('All Sites')
        else:
            # If none of the forms are valid, render the post form template with the forms
            return render(request, 'post_form.html', {'form': form, 'hvac': hvac, 'battery': battery, 'relion': relion, 'contacts': contacts})

def add_post_battery(request):
    """
    Handle the request to add a post about a battery.
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: The response object.
    """
    if request.method == 'GET':
        # Create a context dictionary with the battery form
        context = {'battery': batteryForm()}
        
        # Render the add_post_battery.html template with the context
        return render(request, 'add_post_battery.html', context=context)
    
    elif request.method == 'POST':
        # Create a battery form instance with the POST data
        battery = batteryForm(request.POST)
        
        if battery.is_valid():
            # Save the battery form
            battery.save()
            
            # Redirect to the 'All Sites' page
            return redirect('All Sites')
    
    # If the request method is neither GET nor POST
    else:
    # Render the add_post_battery.html template with the battery form
        return render(request, 'add_post_battery.html', {'battery': battery})
    
def add_post_hvac(request):
    """
    Handle the request to add a post for HVAC.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.method == 'GET':
        # Create the context dictionary with the HVAC form
        context = {'hvac': hvacForm()}
        return render(request, 'add_post_hvac.html', context=context)
    
    elif request.method == 'POST':
        # Create the HVAC form with the POST data
        hvac = hvacForm(request.POST)
        if hvac.is_valid():
            # Save the HVAC form
            hvac.save()
            return redirect('All Sites')
    else:
        # Render the add_post_hvac.html template with the HVAC form
        return render(request, 'add_post_hvac.html', {'hvac': hvac})
    
def add_post_relion(request) :
    """
    Handle GET and POST requests for adding a post related to Relion.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    """
    if request.method == 'GET':
        # Create the context with an instance of the relionForm
        context = {'relion' : relionForm()}
        # Render the add_post_relion.html template with the context
        return render(request, 'add_post_relion.html', context=context)
    
    elif request.method == 'POST':
        # Create an instance of the relionForm with the POST data
        relion = relionForm(request.POST)
        if relion.is_valid():
            # Save the form data to the database
            relion.save()
            # Redirect to the 'All Sites' page
            return redirect('All Sites')
    else:
        # Render the add_post_relion.html template with an instance of the relionForm
        return render(request, 'add_post_relion.html', {'relion' : relion})
    
# TODO: add a view to add contacts
def add_post_contacts(request):
    """
    This function handles the request to add a post contact. It takes in a request object as a parameter.
    The request object contains information about the HTTP request made by the user.

    Parameters:
        - request (HttpRequest): The request object containing information about the HTTP request.

    Returns:
        - HttpResponse: If the request method is 'GET', it renders the 'add_post_contacts.html' template with an instance of the contactsForm and returns the rendered template as an HttpResponse object.
        - HttpResponseRedirect: If the request method is 'POST' and the form data is valid, it saves the form data to the database, and redirects the user to the 'All Sites' page.
        - HttpResponse: If the request method is neither 'GET' nor 'POST', it renders the 'add_post_contacts.html' template with an instance of the contactsForm and returns the rendered template as an HttpResponse object.
    """
    if request.method == 'GET':
        # Create the context with an instance of the contactsForm
        context = {'contacts' : contactsForm()}
        # Render the add_post_contacts.html template with the context
        return render(request, 'add_post_contacts.html', context=context)
    
    elif request.method == 'POST':
        # Create an instance of the contactsForm with the POST data
        contacts = contactsForm(request.POST)
        if contacts.is_valid():
            # Save the form data to the database
            contacts.save()
            # Redirect to the 'All Sites' page
            return redirect('All Sites')
    else:
        # Render the add_post_contacts.html template with an instance of the contactsForm
        return render(request, 'add_post_contacts.html', {'contacts' : contacts})

# add a view to add site_access
def add_post_site_access(request):
    """
    This function handles the request to add a site access. It takes in a request object as a parameter.
    The request object contains information about the HTTP request made by the user.

    Parameters:
        - request (HttpRequest): The request object containing information about the HTTP request.

    Returns:
        - HttpResponse: If the request method is 'GET', it renders the 'add_post_site_access.html' template with an instance of the siteAccessForm and returns the rendered template as an HttpResponse object.
        - HttpResponseRedirect: If the request method is 'POST' and the form data is valid, it saves the form data to the database, and redirects the user to the 'All Sites' page.
        - HttpResponse: If the request method is neither 'GET' nor 'POST', it renders the 'add_post_site_access.html' template with an instance of the siteAccessForm and returns the rendered template as an HttpResponse object.
    """
    if request.method == 'GET':
        # Create the context with an instance of the siteAccessForm
        context = {'site_access': siteAccessForm()}
        # Render the add_post_site_access.html template with the context
        return render(request, 'add_post_site_access.html', context=context)
    
    elif request.method == 'POST':
        # Create an instance of the siteAccessForm with the POST data
        site_access = siteAccessForm(request.POST)
        if site_access.is_valid():
            # Save the form data to the database
            site_access.save()
            # Redirect to the 'All Sites' page
            return redirect('All Sites')
    else:
        # Render the add_post_site_access.html template with an instance of the siteAccessForm
        return render(request, 'add_post_site_access.html', {'site_access': site_access})

# Edit a site's informantion
def edit_post(request, id):
    """
    Edit a post with the given ID.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the post to be edited.

    Returns:
        HttpResponse: The response containing the rendered template.
    """
    post = get_object_or_404(site, site_id=id)

    if request.method == 'GET':
        # Prepare the context with the form and ID
        context = {
            'form': siteForm(instance=post),
            'id': id
        }
        # Render the template with the context
        return render(request, 'post_form.html', context=context)
    elif request.method == 'POST':
        # Process the form data
        form = siteForm(request.POST, instance=post)
        if form.is_valid():
            # Save the form data and display success message
            form.save()
            messages.success(request, 'The Site has been updated successfully.')
            return redirect('Site Display', id=id)
        else:
            # Display error message and render the form template again
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'post_form.html', {'form': form})

def edit_post_hvac(request, id):
    """
    Edit a post about HVAC.

    Args:
        request: The HTTP request object.
        id: The ID of the HVAC site.

    Returns:
        If the request method is GET, render the post edit form.
        If the request method is POST and the form is valid, update the post and redirect.
        If the request method is POST and the form is invalid, render the form with errors.
    """
    postHVAC = get_object_or_404(hvac, hvac_site_id=id)

    if request.method == 'GET':
        context = {
            'formHVAC': hvacForm(instance=postHVAC),
            'id': id
        }
        return render(request, 'post_form_hvac.html', context=context)

    elif request.method == 'POST':
        formHVAC = hvacForm(request.POST, instance=postHVAC)
        if formHVAC.is_valid():
            formHVAC.save()
            messages.success(request, 'The HVAC has been updated successfully.')
            return redirect('Site Display', id=id)
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'post_form_hvac.html', {'formHVAC': formHVAC})

def edit_post_battery(request, id):
    """
    View function to edit a battery post.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The id of the battery post to edit.

    Returns:
        HttpResponse: The HTTP response object.
    """
    # Get the battery post to edit
    postBattery = get_object_or_404(battery, battery_site_id=id)
    
    if request.method == 'GET':
        # Create a form instance with the battery post
        formBattery = batteryForm(instance=postBattery)
        
        # Set the context data for the template
        context = {
            'formBattery' : formBattery,
            'id' : id            
        }
        
        # Render the template with the context data
        return render(request, 'post_form_battery.html', context=context)
    
    elif request.method == 'POST':
        # Create a form instance with the data from the POST request
        formBattery = batteryForm(request.POST, instance=postBattery)
        
        if formBattery.is_valid():
            # Save the form data to the database
            formBattery.save()
            
            # Add a success message to the user
            messages.success(request, 'The Battery Information has been updated successfully.')
            
            # Redirect the user to the 'All Sites' page
            return redirect('Site Display', id=id)
        else:
            # Add an error message and render the template with the form
            messages.error(request, 'Please correct the following errors:')
            return render(request,'post_form_battery.html',{'formBattery' : formBattery})
        
def edit_post_relion(request, id):
    """
    Edit a post in the Relion model.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The id of the post to edit.

    Returns:
        HttpResponse: The HTTP response object.
    """

    # Get the post from the Relion model with the given id
    postRelion = get_object_or_404(relion, relion_site=id)
    
    if request.method == 'GET':
        # Create a context dictionary with the form and id
        context = {
            'formRelion': relionForm(instance=postRelion),
            'id': id
        }
        # Render the post form template with the context
        return render(request, 'post_form_relion.html', context=context)
    
    elif request.method == 'POST':
        # Create a form instance with the request data and the post instance
        formRelion = relionForm(request.POST, instance=postRelion)
        if formRelion.is_valid():
            # Save the form
            formRelion.save()
            # Add a success message
            messages.success(request, 'The Relion Information has been updated successfully.')
            # Redirect to the 'All Sites' page
            return redirect('Site Display', id=id)
        else:
            # Add an error message and render the form template with the form
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'post_form_relion.html', {'formRelion': formRelion})

def edit_post_contacts(request, id):
    """
    Edit the contacts information of a post.
    
    Parameters:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the post.
        
    Returns:
        HttpResponse: The response containing the rendered template.
    """
    postContacts = get_object_or_404(contacts, contact_site_id=id)
    
    if request.method == 'GET':
        # Create a context dictionary with the form and id
        context = {
            'formContacts': contactsForm(instance=postContacts),
            'id': id
        }
        # Render the post form template with the context
        return render(request, 'post_form_contacts.html', context=context)
    
    elif request.method == 'POST':
        # Create a form instance with the request data and the post instance
        formContacts = contactsForm(request.POST, instance=postContacts)
        if formContacts.is_valid():
            # Save the form
            formContacts.save()
            # Add a success message
            messages.success(request, 'The Contacts Information has been updated successfully.')
            # Redirect to the 'All Sites' page
            return redirect('Site Display', id=id)
        else:
            # Add an error message and render the form template with the form
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'post_form_contacts.html', {'formContacts': formContacts})
    
# add a view to edit site_access
def edit_post_site_access(request, id):
    """
    Edit the site access information of a post.
    
    Parameters:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the post.
        
    Returns:
        HttpResponse: The response containing the rendered template.
    """
    postSiteAccess = get_object_or_404(site_access, site_access_site_id=id)
    
    if request.method == 'GET':
        # Create a context dictionary with the form and id
        context = {
            'formSiteAccess': siteAccessForm(instance=postSiteAccess),
            'id': id
        }
        # Render the post form template with the context
        return render(request, 'post_form_site_access.html', context=context)
    
    elif request.method == 'POST':
        # Create a form instance with the request data and the post instance
        formSiteAccess = siteAccessForm(request.POST, instance=postSiteAccess)
        if formSiteAccess.is_valid():
            # Save the form
            formSiteAccess.save()
            # Add a success message
            messages.success(request, 'The Site Access Information has been updated successfully.')
            # Redirect to the 'All Sites' page
            return redirect('Site Display', id=id)
        else:
            # Add an error message and render the form template with the form
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'post_form_site_access.html', {'formSiteAccess': formSiteAccess})



#  Delte a posting/site and its related contents   
def delete_post(request, id):
    """
    Deletes a post and related objects from the database.
    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the post to be deleted.
    Returns:
        HttpResponseRedirect: Redirects to the 'All Sites' page after successful deletion.
    """
    # Get the objects to be deleted from the database
    postToDelete = get_object_or_404(site, site_id=id)
    hvacToDelete = get_object_or_404(hvac, hvac_site_id=id)
    batteryToDelete = get_object_or_404(battery, battery_site_id=id)
    relionToDelete = get_object_or_404(battery, relion_site=id)
    contactsToDelete = get_object_or_404(contacts, contact_site_id=id)
    siteAccessToDelete = get_object_or_404(site_access, site_access_site_id=id)
    
    # Create a context dictionary to be passed to the template
    context = {'postToDelete': postToDelete,
                'hvacToDelete' : hvacToDelete,
                'batteryToDelete' : batteryToDelete,
                'relionToDelete' : relionToDelete,
                'contactsToDelete' : contactsToDelete,
                'siteAccessToDelete' : siteAccessToDelete
               }
    
    if request.method == 'GET':
        # Render the confirmation page for GET requests
        return render(request, 'post_confirm_delete.html', context=context)
    
    elif request.method == 'POST':
        # Delete the objects from the database and display success message
        postToDelete.delete()
        hvacToDelete.delete()
        batteryToDelete.delete()
        relionToDelete.delete()
        contactsToDelete.delete()
        siteAccessToDelete.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('All Sites')
        
def index(request):
    """
    View function for the homepage.
    
    This function takes a request object as input and returns a rendered HTML template.
    It retrieves the count of all sites, generators, and hvacs from the database,
    creates a context dictionary with the count values, and renders the index.html template
    with the context.
    
    Parameters:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: A rendered HTML template.
    """
    # Get the count of all sites
    num_sites = site.objects.all().count()
    
    # Get the count of all generators
    num_generators = generator.objects.all().count()
    
    # Get the count of all hvacs
    num_hvacs = hvac.objects.all().count()
    
    # Create a context dictionary with the count values
    context = {
        'num_sites': num_sites,
        'num_generators': num_generators,
        'num_hvacs': num_hvacs,
    }
    
    # Render the index.html template with the context
    return render(request, 'index.html', context=context)

# To show a site's details
def all_sites(request):
    """
    View function to display all sites.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """
    # Query all sites from the database and retrieve their values
    all_sites = site.objects.all().values()

    # Create a dictionary to hold the context data
    context = {
        'all_sites': all_sites,
    }

    # Render the 'all_sites.html' template with the context data and return the response
    return render(request, 'all_sites.html', context=context)

def show_sites(request, id):
    """
    Renders a template to display site details, HVAC details, HVAC contacts, 
    contact details, generator details, battery details, and relion details 
    for a given site ID.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the site.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """
    siteDetail = site.objects.filter(site_id=id)  # Get site details
    hvacDetail = hvac.objects.filter(hvac_site_id=id)  # Get HVAC details
    hvacContacts = hvac_contacts.objects.filter(hvac_contact_id=id)  # Get HVAC contacts
    contactsDetail = contacts.objects.filter(contact_site_id=id)  # Get contact details
    generatorDetail = generator.objects.filter(generator_id=id)  # Get generator details
    batteryDetail = battery.objects.filter(battery_site_id=id)  # Get battery details
    relionDetail = relion.objects.filter(relion_site=id)  # Get relion details
    siteAccessDetail = site_access.objects.filter(site_access_id=id)  # Get site access details
    
    # print(contactsDetail)
    # print(contactsDetail.first().contact_id)
    # print(contactsDetail.first().contact_site_id.site_id)
    
    context = {
        'siteDetail': siteDetail,
        'hvacDetail': hvacDetail,
        'hvacContacts': hvacContacts,
        'contactsDetail': contactsDetail,
        'generatorDetail': generatorDetail,
        'batteryDetail': batteryDetail,
        'relionDetail': relionDetail,
        'siteAccessDetail': siteAccessDetail
    }
    
    return render(request, 'site_display.html', context=context)
