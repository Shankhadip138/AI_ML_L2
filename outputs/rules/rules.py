def findDecision(obj): #obj[0]: variance, obj[1]: skewness, obj[2]: curtosis, obj[3]: entropy
   # {"feature": "variance", "instances": 1372, "metric_value": 0.1429, "depth": 1}
   if obj[0]>0.43373584747314453:
      # {"feature": "curtosis", "instances": 692, "metric_value": 0.0572, "depth": 2}
      if obj[2]<=0.12563319504261017:
         # {"feature": "skewness", "instances": 350, "metric_value": 0.1797, "depth": 3}
         if obj[1]>6.887003421783447:
            return 0
         elif obj[1]<=6.887003421783447:
            # {"feature": "entropy", "instances": 152, "metric_value": 0.0674, "depth": 4}
            if obj[3]>-2.7518653869628906:
               return 0
            elif obj[3]<=-2.7518653869628906:
               return 1
            else:
               return 0.96
         else:
            return 0.4473684210526316
      elif obj[2]>0.12563319504261017:
         # {"feature": "skewness", "instances": 342, "metric_value": 0.0302, "depth": 3}
         if obj[1]>0.1316792517900467:
            return 0
         elif obj[1]<=0.1316792517900467:
            # {"feature": "entropy", "instances": 158, "metric_value": 0.0428, "depth": 4}
            if obj[3]<=0.009410420432686806:
               return 0
            elif obj[3]>0.009410420432686806:
               return 0
            else:
               return 0.039473684210526314
         else:
            return 0.0189873417721519
      else:
         return 0.008771929824561403
   elif obj[0]<=0.43373584747314453:
      # {"feature": "skewness", "instances": 680, "metric_value": 0.0987, "depth": 2}
      if obj[1]<=6.647108405828476:
         # {"feature": "curtosis", "instances": 552, "metric_value": 0.0181, "depth": 3}
         if obj[2]>-1.8251733779907227:
            # {"feature": "entropy", "instances": 488, "metric_value": 0.008, "depth": 4}
            if obj[3]>-3.672169327735901:
               return 1
            elif obj[3]<=-3.672169327735901:
               return 1
            else:
               return 1.0
         elif obj[2]<=-1.8251733779907227:
            return 1
         else:
            return 1.0
      elif obj[1]>6.647108405828476:
         # {"feature": "curtosis", "instances": 128, "metric_value": 0.054, "depth": 3}
         if obj[2]<=2.156300574541092:
            # {"feature": "entropy", "instances": 106, "metric_value": 0.0722, "depth": 4}
            if obj[3]<=-2.6541457176208496:
               return 0
            elif obj[3]>-2.6541457176208496:
               return 0
            else:
               return 0.0
         elif obj[2]>2.156300574541092:
            return 0
         else:
            return 0.0
      else:
         return 0.2578125
   else:
      return 0.7926470588235294
