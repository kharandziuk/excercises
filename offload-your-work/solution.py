def work_needed(project_minutes, freelancers):
    freelancers_sum = sum((h * 60 + m) for h, m in freelancers)
    diff = project_minutes - freelancers_sum
    if diff <= 0:
        return 'Easy Money!'
    else:
        hours = diff // 60
        minutes = diff % 60
        return 'I need to work %d hour(s) and %d minute(s)' % (hours, minutes)

if __name__ == '__main__':
    assert(work_needed(60, [(1,0)]) == "Easy Money!")
    assert(work_needed(60, [(0,0)]) =="I need to work 1 hour(s) and 0 minute(s)")
    assert(work_needed(141, [(1,55), (0,25)]) == "I need to work 0 hour(s) and 1 minute(s)")
    print('done')
