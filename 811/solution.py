class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = {}
        for domain in cpdomains:
            count, full_domain = domain.split()
            subdomains = full_domain.split('.')[::-1]
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[:i+1][::-1])
                counts[subdomain] = counts.get(subdomain, 0) + int(count)
        return [f'{count} {subdomain}' for subdomain, count in counts.items()]