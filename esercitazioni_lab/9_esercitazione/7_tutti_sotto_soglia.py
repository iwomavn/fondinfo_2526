def all_below(data, limit):
    if len(data) == 0:
        return True
    
    if data.pop(0) > limit:
        return False
    else:
        return all_below(data, limit)
    
def main():
    print(all_below([0, 1, 2, 3, 5, 6], 8))
    print(all_below([10, 9, 8, 6, 7], 9))
    print(all_below([8, 4, 6, 11, 7], 9))
    
if __name__ == "__main__":
    main()
