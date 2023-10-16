# DjangoRunbook

## Error List + Fixes 

 ###### Author/Coder: Evan Toland 

---

### Some common errors
**Error:**  *That ==port== is already in use.*

> **Solution:**  `ps -ef | grep python | grep 8001`
>**Returns:**

>> ```
>>etoland 398447 398261 0 Sep13 pts/61 00:00:00 python manage.py runserver {webiste IP}:8001
>>etoland 403186 398447 0 15:52 pts/61 00:00:01 /django-project/venv/bin/python manage.py runserver {webiste IP}:8001
>> ```

>**Solution:** kill 398447 
>>**Note:** number will be different when a different individual runs `grep` cmd

  

**Error:**  *NoPermissions (FileSystemError): Error: EACCES: permission denied, open '/django-project/site/logs/help'*

>**Solution:**  `sudo chown -R {user} {directory path}`

    
service apache2 restart

python manage.py makemigrations
    python manage.py migrate
        python manage.py runserver {webiste IP}:8001

[![built with Codeium](https://codeium.com/badges/main)](https://codeium.com)
